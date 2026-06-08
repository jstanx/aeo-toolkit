#!/usr/bin/env python3
"""
Run a prompt set across AI engines and log whether the brand and competitors are
mentioned/cited, then summarize share of voice. Pure standard library (uses urllib for
HTTP). Engines are enabled only when their API key is present, so this runs gracefully
with no keys.

Usage:
  python test_prompts.py --selftest             # verify detection logic offline
  python test_prompts.py --sample               # print an example prompts config
  python test_prompts.py --input prompts.json   # run against configured engines
  python test_prompts.py --input prompts.json --csv results.csv

Config JSON:
  {"brand": "Acme", "competitors": ["Beta", "Gamma"],
   "prompts": ["best product analytics for B2B SaaS", "Acme vs Beta"]}

Engines & env keys (set the ones you want to test):
  OpenAI       OPENAI_API_KEY        (model: OPENAI_MODEL, default gpt-4o-mini)
  Anthropic    ANTHROPIC_API_KEY     (model: ANTHROPIC_MODEL, default claude-sonnet-4-6)
  Perplexity   PERPLEXITY_API_KEY    (model: PERPLEXITY_MODEL, default sonar)

Caveat: base chat models answer from training data; engines with live web search
(e.g. Perplexity, or browsing-enabled variants) better reflect real AI-search citations.
See ../templates/tracking-sheet.md and ../SKILL.md.
"""

import argparse
import csv
import json
import os
import re
import sys
import urllib.request

SAMPLE = {"brand": "Acme", "competitors": ["Beta", "Gamma"],
          "prompts": ["best product analytics for B2B SaaS", "Acme vs Beta"]}

URL_RE = re.compile(r"https?://[^\s)\]>\"']+")


def detect(answer, brand, competitors, extra_citations=None):
    low = answer.lower()
    brand_hit = brand.lower() in low
    comp_hits = [c for c in competitors if c.lower() in low]
    cites = set(URL_RE.findall(answer)) | set(extra_citations or [])
    return {"brand_mentioned": brand_hit, "competitors_mentioned": comp_hits,
            "n_citations": len(cites)}


def _post(url, headers, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def call_openai(prompt):
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        return None
    body = {"model": os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
            "messages": [{"role": "user", "content": prompt}]}
    res = _post("https://api.openai.com/v1/chat/completions",
                {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, body)
    return res["choices"][0]["message"]["content"], []


def call_anthropic(prompt):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        return None
    body = {"model": os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6"),
            "max_tokens": 1024, "messages": [{"role": "user", "content": prompt}]}
    res = _post("https://api.anthropic.com/v1/messages",
                {"x-api-key": key, "anthropic-version": "2023-06-01",
                 "Content-Type": "application/json"}, body)
    return "".join(b.get("text", "") for b in res.get("content", [])), []


def call_perplexity(prompt):
    key = os.environ.get("PERPLEXITY_API_KEY")
    if not key:
        return None
    body = {"model": os.environ.get("PERPLEXITY_MODEL", "sonar"),
            "messages": [{"role": "user", "content": prompt}]}
    res = _post("https://api.perplexity.ai/chat/completions",
                {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}, body)
    text = res["choices"][0]["message"]["content"]
    return text, res.get("citations", [])


ENGINES = {"openai": call_openai, "anthropic": call_anthropic, "perplexity": call_perplexity}
ENV_KEY = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY",
           "perplexity": "PERPLEXITY_API_KEY"}


def selftest():
    ans = ("For B2B SaaS, Acme is a strong choice; some teams also like Beta. "
           "See https://example.com/guide and https://acme.com.")
    r = detect(ans, "Acme", ["Beta", "Gamma"])
    assert r["brand_mentioned"] is True
    assert r["competitors_mentioned"] == ["Beta"]
    assert r["n_citations"] == 2
    r2 = detect("Gamma and Beta lead the market.", "Acme", ["Beta", "Gamma"])
    assert r2["brand_mentioned"] is False
    assert set(r2["competitors_mentioned"]) == {"Beta", "Gamma"}
    print("selftest OK — detection logic verified")


def main():
    ap = argparse.ArgumentParser(description="Run a prompt set across AI engines")
    ap.add_argument("--input", help="path to prompts config JSON")
    ap.add_argument("--csv", help="write per-result rows to this CSV file")
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if args.sample:
        print(json.dumps(SAMPLE, indent=2))
        return
    if not args.input:
        ap.error("provide --input <config.json>, or --sample / --selftest")

    cfg = json.load(open(args.input, encoding="utf-8"))
    brand, competitors = cfg["brand"], cfg.get("competitors", [])
    prompts = cfg["prompts"]

    active = [name for name in ENGINES if os.environ.get(ENV_KEY[name])]
    if not active:
        print("No engine API keys set. Set one or more of OPENAI_API_KEY, "
              "ANTHROPIC_API_KEY, PERPLEXITY_API_KEY and re-run.")
        print("Tip: run --selftest to verify the detection logic without any keys.")
        return

    rows = []
    brand_hits = {e: 0 for e in active}
    name_counts = {e: {"_brand": 0, **{c: 0 for c in competitors}} for e in active}
    for engine in active:
        for prompt in prompts:
            try:
                result = ENGINES[engine](prompt)
            except Exception as e:  # noqa: BLE001
                print(f"[{engine}] error on {prompt!r}: {e}", file=sys.stderr)
                continue
            if result is None:
                continue
            answer, cites = result
            d = detect(answer, brand, competitors, cites)
            rows.append({"engine": engine, "prompt": prompt,
                         "brand_mentioned": d["brand_mentioned"],
                         "competitors_mentioned": ";".join(d["competitors_mentioned"]),
                         "n_citations": d["n_citations"]})
            brand_hits[engine] += d["brand_mentioned"]
            name_counts[engine]["_brand"] += d["brand_mentioned"]
            for c in d["competitors_mentioned"]:
                name_counts[engine][c] += 1

    print(f"\nPrompt-set results — brand: {brand}\n")
    for engine in active:
        total = sum(name_counts[engine].values())
        sov = (100 * name_counts[engine]["_brand"] / total) if total else 0
        print(f"{engine}: brand mentioned {brand_hits[engine]}/{len(prompts)} prompts, "
              f"share of voice {sov:.0f}%")

    if args.csv and rows:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        print(f"\nWrote {len(rows)} rows to {args.csv}")


if __name__ == "__main__":
    main()
