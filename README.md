[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/JoeyAlexander21/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/JoeyAlexander21/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the [make.fun bounty "Sum up 25 November's world news in one image"](https://make.fun/bounty/news-image-20261125) — $100 in USDC, shared by the top 50 entries.

# The World Today — 25 November 2026 in one image

Entry for the make.fun bounty `news-image-20261125`: sum up the world's
news of **Wednesday, 25 November 2026** in one image.

The image is a one-page newspaper front page (`entry.png`, 1024×1024,
~157 KB): a masthead with the date in a navy banner, a lead story with a
drawn illustration, five more stories in a grid, and an "Also today" box.
Every story names what happened and a checkable number; the footer names
the sources. It was drawn in code (PIL, see `build_image.py`) so all text
is exact and legible, and the result was inspected visually.

## Stories chosen (all first reported on 25 Nov 2026 in at least one time zone)

| # | Story | Key facts on the page | Sources |
|---|-------|----------------------|---------|
| 1 | **Houthi drone hits Riyadh's tallest tower** (lead) | 2nd strike on the PIF HQ tower in under a week; 11 injured — 2 Saudis, 2 Indians, 3 Nepalese, 4 Egyptians; coalition vows a "decisive" response | Reuters (via BusinessWorld, 25 Nov), Saudi Civil Defence / SPA |
| 2 | **Australia's inflation jumps to 4.9%** | CPI +4.9% y/y to Oct (from 4.3% in Sep), released 25 Nov 00:30 GMT; electricity +25.2%; trimmed mean 3.8% | Australian Bureau of Statistics, 25 Nov 2026 |
| 3 | **Zelenskyy: Ukraine hit Russian ship** | Kyiv says its drone struck cargo ship *Sparta II* in the Gulf of Finland on 21 Nov; Zelenskyy called it a legitimate target; Norway urged caution | Reuters / Bloomberg, 24 Nov (reported widely 25 Nov) |
| 4 | **Huawei guilty of stealing trade secrets** | New York jury: guilty on 10 of 12 counts incl. trade-secret conspiracy and bank fraud; acquitted of racketeering; Huawei will appeal | AP, Reuters, 24 Nov (US) / 25 Nov (Asia) |
| 5 | **CIA and ODNI hit by cyberattack** | Unclassified system breached; no classified information affected; breach resolved | AP / Reuters / CNN, 24–25 Nov |
| 6 | **Trump gives Giuliani the Medal of Freedom** | Awarded in an Oval Office ceremony on Tuesday | AP / Reuters, 24 Nov (US) / 25 Nov (Asia) |

Also today (footer box): Sarkozy corruption case ordered to trial in
France; 25 Nov is the International Day for the Elimination of Violence
against Women; Trump pardons Thanksgiving turkeys Freedom and Feathers.

Deliberately **not** included: the Villavicencio (Colombia) car bomb —
it happened on the evening of 23 Nov local time, so it is 23–24 Nov news,
not 25 Nov.

Date note: the bounty counts events that happened or were first reported
on 25 November 2026 **in any time zone**. Several US stories above broke
on Tuesday 24 Nov in New York but on Wednesday 25 Nov in Asia/Australia;
the page says "reported on 25 November 2026 in at least one time zone"
and never claims a US date for them. The one story dated squarely 25 Nov
everywhere is the Australian CPI release.

## Files

- `main.ts` — Node 22, standard library only. Copies `entry.png` to
  `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). No network,
  deterministic.
- `entry.png` — the image (1024×1024 PNG).
- `build_image.py` — the generator that drew `entry.png` (PIL only).
  Re-run with `python3 build_image.py` to regenerate it identically.
- `LICENSE` — MIT (from the kit's starter).

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# check: out/entry.png is a 1024x1024 PNG under 1 MiB
```

Run it twice and compare sha256 — both runs must write identical bytes.

## What is still missing to submit

This workspace is **local only**. To submit, the owner still has to:

1. Create a public GitHub repo (created after the competition opened,
   25 Nov 2026 00:00 UTC) under their own account, with an OSI-approved
   license, and push this directory to it.
2. Make the transcript bundle with the kit CLI
   (`node cli/makefun.mjs bundle`, run from inside the unpacked kit) —
   it must cover **this** session and its parent session.
3. Submit the repo URL + commit SHA + bundle on make.fun before the
   deadline **27 Nov 2026 00:00 UTC (07:00 WIB)**. No submission has been
   made from this session.
