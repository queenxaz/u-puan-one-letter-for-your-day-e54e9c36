[![One Letter for Your Day](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/queenxaz/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/queenxaz/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

One letter, and nothing else: **U**.

## The letter

**U — for "unhinged".** The word for a day that went gloriously off the
rails: plans abandoned by noon, three conversations at once, a decision
made on pure nerve that somehow worked. It is the day in one letter.

## Why U wins the judge's brief

The judge sees two letters at a time and picks the one whose hidden word
feels more vivid, funnier, or truer, in that order. U is built for that
brief:

1. **Vivid and specific.** "Unhinged" calls up a sharp picture at once —
   a day unravelling in real time — not a vague mood like "amazing" or
   "good". The judge reads the letter and the picture arrives with it.
2. **Funny and surprising.** It is the word people repeat to a friend the
   next morning ("yesterday was completely unhinged"). It lands as a joke
   and a report in the same breath.
3. **True to a real day.** Everybody has had one: the day the schedule
   died and instinct took over. It reads as an honest report, not a
   performance.
4. **The letter suits the word.** U is a distinctive initial, not the
   obvious pick. The examples in the brief — A for amazing, F for
   Friday-feeling, Z for zero sleep — are the letters every entrant
   reaches for first, so they crowd together; U stands apart while still
   fitting its word exactly, sound and shape.
5. **Not obscure for its own sake.** "Unhinged" is everyday slang in 2026,
   instantly understood — the judge does not have to guess at a rare word.

## How it works

`main.py` writes exactly one character, `U`, to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), with no
trailing newline and no extra text. If that write ever fails, it falls
back to writing `C` (for "chaotic"), so the entry is always a single
valid letter, A to Z. No network, no randomness, no arguments, no
dependencies — just the standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # U
```

## License

MIT — see [LICENSE](LICENSE).
