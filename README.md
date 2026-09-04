# period-watch

This CLI app tracks which school period is currently on, and when it will end.

# Credit

This program was made during TP course in UTM.
It also uses typical UTM schedule.

# Requirements

This program uses pyenv to manage its python version.

It requires python 3.13.11 to work.

# Usage

## Setup the workspace

```bash
> git clone https://github.com/ra1nlox/period-watch.git

> cd period-watch

> python -m venv --without-scm-ignore-files ./

> source ./bin/activate # or whatever you use

> pyenv install # or, if you already have it, it should work automatically
```

## Use the program

```bash
> python main.py
```

## Example of `tt.txt`

Note that period (and pause) names can be whatever you want.
The most important "syntactic" parts are ": " and " - ", as they are used to split strings.

```
PERIOD 1: 8:00 - 9:30
PAUSE: 9:30 - 9:45
PERIOD 2: 9:45 - 11:15
PAUSE: 11:15 - 11:30
PERIOD 3: 11:30 - 13:00
PAUSE: 13:00 - 13:30
PERIOD 4: 13:30 - 15:00
PAUSE: 15:00 - 15:15
PERIOD 5: 15:15 - 16:45
PAUSE: 16:45 - 17:00
PERIOD 6: 17:00 - 18:30
PAUSE: 18:30 - 18:45
PERIOD 7: 18:45 - 20:15
```