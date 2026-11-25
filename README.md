# The Robot Apology

[![The Robot Apology](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/aurorabelle788/u-suga-the-robot-apology-dd96bb59-v1/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)
[![Reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/aurorabelle788/u-suga-the-robot-apology-dd96bb59-v1/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59)

A two-line robot confession for the [make.fun bounty "The Robot Apology"](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59).

## What it does

`main.py` writes one short text to `/output/entry.txt`: a robot apologising
in a single sentence for one specific, concrete mistake — replying-all to
the whole office with a birthday message meant for one person — and a second
sentence saying what it learned and what it will do differently.

## Run

```sh
python3 main.py
```

Standard library only, Python 3.13. Deterministic: the same bytes every run.
No network, no randomness, no file reads outside this repository.
