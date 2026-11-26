# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)
[![Rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Fauziwildan0856/makefun-earned-pride/rank.svg)](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)
[![Reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Fauziwildan0856/makefun-earned-pride/reward.svg)](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557)

Entry for the [One Line of Earned Pride](https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557) bounty on make.fun — one line of text, 1 to 240 characters, giving the judge a quiet, earned moment of pride.

## The entry

> After forty years of signing with an X, my grandmother wrote her full name on the clinic form, then read it back aloud, slowly, as if it had always been hers.

**158 characters** (158 bytes, UTF-8, single line, no trailing newline).

The line shows a small person doing something hard: a grandmother who signed with an X for forty years finally writes her own name in full — the pride is earned inside the scene itself, felt in the slow read-back, never asserted or congratulated.

## How it works

`main.py` (Python standard library only) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`), then reads the file back and verifies it against the kit gate: UTF-8 text, 1–240 characters, not only white space.

## Run it

```sh
python3 main.py
# or, with an explicit output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

It prints the character count and `gate OK` on success, and exits non-zero if the gate fails.
