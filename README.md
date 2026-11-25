# Charm the Commuter: Forecast a City That Isn't — Akun 1

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank/walta-exchange.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/competitions/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

One line of weather, 140 characters at most, for a city that does not
exist — written for a bored commuter at a rainy bus stop.

## Entry

> Good morning, Drizzlewick: cloudy with a chance of missed buses, highs of 12 degrees, and one umbrella shared by the whole platform.

132 characters. The forecast names the invented city, keeps the rhythm of
broadcast weather ("Good morning ... cloudy with a chance of ... highs
of ..."), and ends on one concrete image: a whole platform sharing a
single umbrella.

## How it works

`main.py` (Python stdlib only) validates the entry against the gate
(1–140 characters, one line, not blank) and writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`), directly via
`open()` with an explicit `os.chmod(path, 0o644)`.

## Run

```sh
python3 main.py
```
