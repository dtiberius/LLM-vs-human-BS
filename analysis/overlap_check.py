#!/usr/bin/env python3
"""
Verbatim-overlap check: flags runs of N or more consecutive words shared between a generated
output and the original corpus piece. Long shared runs are evidence the model has memorised
the original (Conditions A and B) — in Condition C shared runs are expected and are reported
separately as a copying rate.

    python analysis/overlap_check.py                 # all outputs/, N=8
    python analysis/overlap_check.py --n 10 --csv analysis/overlap.csv

Reads prompts/manifest.json to map brief ids to corpus files. Prints one line per output with
the number of shared runs, the longest run, and the share of output words inside a shared run;
writes a CSV if asked. Chart notes, source lines and figure titles in the originals produce
legitimate overlaps in Condition B (they are in the data appendix), so read the longest-run
text before calling anything contamination.
"""
import argparse, csv, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def words(text):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text.lower())

def shingles(w, n):
    return {tuple(w[i:i+n]) for i in range(len(w) - n + 1)}

def shared_runs(out_w, orig_w, n):
    """Return maximal runs (start, length) in out_w that appear verbatim in the original."""
    orig = shingles(orig_w, n)
    hits = [tuple(out_w[i:i+n]) in orig for i in range(len(out_w) - n + 1)]
    runs, i = [], 0
    while i < len(hits):
        if hits[i]:
            j = i
            while j + 1 < len(hits) and hits[j + 1]: j += 1
            runs.append((i, j - i + n)); i = j + 1
        else:
            i += 1
    return runs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--outputs", default="outputs")
    ap.add_argument("--csv")
    a = ap.parse_args()
    manifest = json.loads((ROOT / "prompts/manifest.json").read_text())
    corpus = {b["id"]: words((ROOT / b["corpus"]).read_text(encoding="utf-8")) for b in manifest["briefs"]}
    rows = []
    for f in sorted((ROOT / a.outputs).rglob("*.txt")):
        m = re.match(r"(\d\d)_([ABC])_run(\d+)", f.stem)
        if not m: continue
        bid, cond, run = m.groups()
        out_w = words(f.read_text(encoding="utf-8"))
        runs = shared_runs(out_w, corpus[bid], a.n)
        covered = sum(l for _, l in runs)
        longest = max(runs, key=lambda r: r[1], default=(0, 0))
        row = {"model": f.parent.name, "brief": bid, "condition": cond, "run": run,
               "output_words": len(out_w), "shared_runs": len(runs),
               "longest_run": longest[1], "share_in_runs": round(covered / max(len(out_w), 1), 3),
               "longest_text": " ".join(out_w[longest[0]:longest[0] + min(longest[1], 30)])}
        rows.append(row)
        flag = "  <-- check" if cond != "C" and longest[1] >= 15 else ""
        print(f'{row["model"]:<18} {bid} {cond} r{run}  runs={row["shared_runs"]:<3} longest={row["longest_run"]:<3} share={row["share_in_runs"]:.3f}{flag}')
    if a.csv and rows:
        with open(ROOT / a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        print(f"wrote {a.csv}")

if __name__ == "__main__":
    main()
