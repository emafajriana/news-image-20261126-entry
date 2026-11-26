# The World Today — 26 November 2026

[![news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126/)
[![rank](https://make.fun/badge/news-image-20261126/emafajriana/news-image-20261126-entry/rank.svg)](https://make.fun/c/news-image-20261126/)
[![reward](https://make.fun/badge/news-image-20261126/emafajriana/news-image-20261126-entry/reward.svg)](https://make.fun/c/news-image-20261126/)

One image summing up the world's news of Thursday 26 November 2026:
a dense front page with 4 hero stories and 28 more in the World
Briefing — 32 dated stories across 9 regions, from the Strait of
Hormuz to the Solomons, built for the
[make.fun](https://make.fun/c/news-image-20261126/) competition
"Sum up 26 November's world news in one image".

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory, verifying the PNG signature,
the 1024×1024 dimensions and the sha256 before writing, then
reading the output back byte-for-byte.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The image

`entry.png` — 1024×1024, a front page dated Thursday 26 November 2026.
Heroes: mines in the Strait of Hormuz, the Houthi strike on Saudi
Arabia's Ras Tanura refinery, Ukraine's strikes on two Rosneft
refineries, and Huawei's conviction in Brooklyn. The World Briefing
covers the Dow topping 50,000, Asia's market slide, the Gaza and
Sudan wars, the Solomons treaty, Shenzhou-24, COP31, and more.
Every story is a real event from 25–26 November 2026; sources are
listed in `STATE.md` (build record, not shipped in the repo).

## License

MIT — see [LICENSE](LICENSE).
