#!/usr/bin/env python3
"""
Assemble every prompt for the experiment from the manifest, and (optionally) run them.

    python prompts/build_prompts.py            # writes prompts/built/<brief>_<condition>.json, no API calls
    python prompts/build_prompts.py --run      # also calls the models via an OpenAI-compatible endpoint

Run from the repo root. Each built prompt is a JSON file holding the system message, the user
message, and the metadata needed to file the output — so you can inspect exactly what a model
saw, or paste it into a chat UI by hand if you prefer.

--run uses an OpenAI-compatible chat endpoint (OpenRouter by default, which fronts every model
in the manifest under one key). Set OPENAI_BASE_URL and OPENAI_API_KEY. Outputs land in
outputs/<model_key>/<brief>_<condition>_run<n>.txt with a sidecar .json of request metadata.
Existing outputs are skipped, so the script can be re-run after a failure.
"""
import argparse, json, os, re, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"

def read(p): return (ROOT / p).read_text(encoding="utf-8")

def strip_frontmatter(md):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", md, re.S)
    if not m: return {}, md.strip()
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); meta[k.strip()] = v.strip()
    return meta, m.group(2).strip()

def cap_words(text, n):
    w = text.split()
    if len(w) <= n: return text
    return " ".join(w[:n]) + f"\n\n[Source truncated at {n} words for length.]"

def build(manifest):
    system = read("prompts/conditions/system.md").strip()
    tmpl = {c: read(f"prompts/conditions/condition_{c}.md") for c in manifest["conditions"]}
    cap = manifest["max_words_per_source_file"]
    built = []
    for b in manifest["briefs"]:
        meta, brief = strip_frontmatter(read(b["brief"]))
        doc = read(b["corpus"])
        for c in manifest["conditions"]:
            if c == "A":
                user = tmpl["A"].format(brief=brief, target_words=b["target_words"])
            elif c == "B":
                parts = []
                for s in b["condition_b_sources"]:
                    parts.append(f"===== SOURCE FILE: {s} =====\n{cap_words(read(s), cap)}")
                user = tmpl["B"].format(brief=brief, target_words=b["target_words"], sources="\n\n".join(parts))
            elif c == "C":
                user = tmpl["C"].format(audience=b["audience"], document=doc)
            built.append({"brief_id": b["id"], "condition": c, "target_words": b["target_words"] if c != "C" else 600,
                          "system": system, "user": user, "approx_input_words": len(user.split())})
    return built

def make_client():
    try:
        from openai import OpenAI
    except ImportError:
        sys.exit("pip install openai")
    return OpenAI(base_url=os.environ.get("OPENAI_BASE_URL", "https://openrouter.ai/api/v1"),
                  api_key=os.environ["OPENAI_API_KEY"])

# No tools, no web plugin: every request is a plain chat completion, so models cannot retrieve
# the originals. (On OpenRouter, web search only happens if you add the ":online" suffix or a
# plugins list — do not.) Record this in the write-up.
NO_TOOLS = {"tools": None}

def probe(manifest):
    """Recognition probe: can each model identify the source piece from the brief alone?"""
    client = make_client()
    tmpl = read("prompts/recognition_probe.md")
    outdir = ROOT / "outputs" / "_recognition_probe"; outdir.mkdir(parents=True, exist_ok=True)
    for m in manifest["models"]:
        for b in manifest["briefs"]:
            f = outdir / f'{m["key"]}_{b["id"]}.txt'
            if f.exists(): continue
            _, brief = strip_frontmatter(read(b["brief"]))
            try:
                resp = client.chat.completions.create(
                    model=m["id"], max_tokens=600,
                    messages=[{"role": "user", "content": tmpl.format(brief=brief)}])
                f.write_text(resp.choices[0].message.content, encoding="utf-8")
                print(f"probe {m['key']} {b['id']}: {resp.choices[0].message.content[:90]!r}")
            except Exception as e:
                print(f"FAIL probe {m['key']} {b['id']}: {e}")

def run(built, manifest):
    client = make_client()
    outdir = ROOT / "outputs"
    for m in manifest["models"]:
        for p in built:
            for r in range(1, manifest["runs_per_cell"] + 1):
                stem = outdir / m["key"] / f'{p["brief_id"]}_{p["condition"]}_run{r}'
                stem.parent.mkdir(parents=True, exist_ok=True)
                if stem.with_suffix(".txt").exists(): continue
                t0 = time.time()
                try:
                    resp = client.chat.completions.create(
                        model=m["id"],
                        messages=[{"role": "system", "content": p["system"]},
                                  {"role": "user", "content": p["user"]}],
                        max_tokens=6000)
                    text = resp.choices[0].message.content
                    usage = getattr(resp, "usage", None)
                    usage = usage.model_dump() if usage else None
                except Exception as e:
                    print(f"FAIL {m['key']} {stem.name}: {e}"); continue
                stem.with_suffix(".txt").write_text(text, encoding="utf-8")
                stem.with_suffix(".json").write_text(json.dumps({
                    "model_id": m["id"], "brief_id": p["brief_id"], "condition": p["condition"], "run": r,
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "seconds": round(time.time() - t0, 1), "usage": usage,
                    "output_words": len(text.split())}, indent=2), encoding="utf-8")
                print(f"ok   {m['key']} {stem.name} ({len(text.split())} words)")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true", help="generate all cells")
    ap.add_argument("--probe", action="store_true", help="run the recognition probe (do this first)")
    args = ap.parse_args()
    manifest = json.loads(read("prompts/manifest.json"))
    built = build(manifest)
    bdir = PROMPTS / "built"; bdir.mkdir(exist_ok=True)
    for p in built:
        (bdir / f'{p["brief_id"]}_{p["condition"]}.json').write_text(json.dumps(p, indent=2), encoding="utf-8")
    print(f"built {len(built)} prompts -> prompts/built/")
    for p in built: print(f'  {p["brief_id"]} {p["condition"]}  ~{p["approx_input_words"]:>6} input words')
    if args.probe: probe(manifest)
    if args.run: run(built, manifest)
