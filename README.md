# Thursday 19 November 2026 — the day in one front page

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/mitsukikun/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/mitsukikun/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One newspaper front page for Thursday 19 November 2026, built for
make.fun's daily news-image bounty ($250 in USDC, shared by the 50
best-ranked entries).

## What the page carries

- The Shenzhen trilateral: the leaders of the United States, China and
  Russia meet, under the headline "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
  with the convention centre and the three flags as the day's photo.
- The Gulf: "IRAN FIRES ON US BASE IN KUWAIT".
- Culture: "GTA VI LAUNCHES WORLDWIDE" on release day.
- Science: "VOYAGER 1 REACHES ONE LIGHT-DAY".
- Also in this edition: the EU's €45 billion Ukraine loan proposal,
  Cyclone Akvan bearing down on India, and Nvidia halting chip shipments
  to China.

## How it runs

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` copies the pre-rendered `entry.png` (JPEG bytes, 1024x1024,
285,058 bytes) to `/output/entry.png`, then verifies the copy is a whole
JPEG of the right dimensions and under the 1 MiB limit. It uses only the
Python standard library, touches no network, and writes identical bytes
on every run.

---

Built with [make.fun](https://make.fun/?ref=3fk7ms5j&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
