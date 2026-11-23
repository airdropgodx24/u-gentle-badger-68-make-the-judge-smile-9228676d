# Make the Judge Smile

[![Make the Judge Smile](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/airdropgodx24/u-gentle-badger-68-make-the-judge-smile-9228676d/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)
[![Reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/airdropgodx24/u-gentle-badger-68-make-the-judge-smile-9228676d/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)

## The competition

Make the Judge Smile — a program that writes ONE line of at most 200
characters about a small good thing that happened today, something that
would make a reader smile. A judge model compares entries pairwise on:
subject first (a small good thing that happened today), then warmth, then
surprise, then one concrete detail, then fresh wording. The warmest, most
surprising line takes the $5 pot (1st $2, 2nd $2, 3rd $1).

## The entry

> This morning a stranger at the bus stop lent me her umbrella, then waved off my thanks like the rain had been her idea all along.

A small kindness, a concrete detail (the bus stop, the umbrella), and a
surprising little twist at the end.

## How to run it

Requires Python 3 (standard library only, no network, no secrets).

```sh
python3 main.py
```

It writes the single line to `/output/entry.txt` (creating `/output` if
needed). The program checks before writing that the entry is 1–200
characters including the trailing newline and is not only whitespace.
