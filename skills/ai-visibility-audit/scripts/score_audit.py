#!/usr/bin/env python3
"""
Score an AEO audit against the five-dimension rubric and print a report.
Pure standard library.

Usage:
  python score_audit.py --template          # print a blank input to fill in
  python score_audit.py --input scores.json # compute total, stage, and report

Input JSON: each dimension scored 0–3 with optional notes.
  {
    "discoverability":   {"score": 2, "notes": "..."},
    "interpretability":  {"score": 1, "notes": "..."},
    "attribution":       {"score": 2, "notes": "..."},
    "authority":         {"score": 1, "notes": "..."},
    "governance":        {"score": 3, "notes": "..."}
  }
See ../../../references/aeo-audit-rubric.md for what each dimension means.
"""

import argparse
import json
import sys

DIMENSIONS = ["discoverability", "interpretability", "attribution", "authority", "governance"]

TEMPLATE = {d: {"score": 0, "notes": ""} for d in DIMENSIONS}


def stage(total):
    # total out of 15
    if total <= 3:
        return "Invisible"
    if total <= 8:
        return "Emerging"
    if total <= 12:
        return "Established"
    return "Authority"


def main():
    ap = argparse.ArgumentParser(description="Score an AEO audit (0–3 per dimension)")
    ap.add_argument("--input", help="path to JSON scores")
    ap.add_argument("--template", action="store_true", help="print a blank input")
    args = ap.parse_args()

    if args.template:
        print(json.dumps(TEMPLATE, indent=2))
        return
    if not args.input:
        ap.error("provide --input <scores.json> or --template")

    data = json.load(open(args.input, encoding="utf-8"))
    total = 0
    rows = []
    for d in DIMENSIONS:
        entry = data.get(d) or {}
        score = entry.get("score")
        if not isinstance(score, int) or not (0 <= score <= 3):
            sys.exit(f"dimension '{d}': score must be an integer 0–3 (got {score!r})")
        total += score
        rows.append((d, score, entry.get("notes", "")))

    print("AEO Readiness Audit\n")
    print(f"{'dimension':<18} {'score':<6} notes")
    print("-" * 60)
    for d, s, notes in rows:
        print(f"{d:<18} {s}/3    {notes}")
    print("-" * 60)
    print(f"{'TOTAL':<18} {total}/15")
    print(f"\nMaturity stage: {stage(total)}")

    weakest = [d for d, s, _ in rows if s == min(r[1] for r in rows)]
    print(f"Weakest dimension(s) to prioritize: {', '.join(weakest)}")
    print("\nNext: turn the lowest-scoring dimensions into a prioritized fix list, "
          "mapping each to the owning skill.")


if __name__ == "__main__":
    main()
