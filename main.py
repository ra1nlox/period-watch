import sys
import time
from datetime import datetime

TICK = 1


def parse_total_seconds(time_str: str) -> int:
    parts = list(map(int, time_str.split(":")))

    if len(parts) == 2:
        hours, minutes = parts
        return hours * 3600 + minutes * 60
    else:
        raise ValueError(f'Invalid time format: "{time_str}". Required format XX:XX')


class Period:
    def __init__(self, starts_at, ends_at, name):
        self.start = starts_at
        self.start_c = parse_total_seconds(starts_at)
        self.end = ends_at
        self.end_c = parse_total_seconds(ends_at)
        self.name = name

    def __repr__(self):
        return f"{self.name}: {self.start} - {self.end}"


def main():

    periods = []

    with open("tt.txt") as f:
        lines = f.readlines()

    for l in lines:
        name, period = l.split(": ", maxsplit=1)
        start, end = period.split(" - ")
        periods.append(Period(start, end, name))

    # for p in periods:
    #     print(f"{p.start_c} - {p.end_c}")

    # print(f"Current tickrate: {TICK}")
    while True:
        now = datetime.now()

        seconds_today = (now.hour * 3600) + (now.minute * 60) + now.second
        for p in periods:
            # Se verifică dacă perechile nu s-au ănceput
            if periods.index(p) == 0 and seconds_today <= p.start_c:
                print(
                    f"1st period will start in:  {(p.end_c - seconds_today) // 60}:{(p.end_c - seconds_today) % 60:02d}"
                )
            # Se verifică perechea/pauza curentă
            elif seconds_today >= p.start_c and seconds_today <= p.end_c:
                print(f"Current period: {p.name}")
                print(
                    f"Minutes:seconds till the end: {(p.end_c - seconds_today) // 60}:{(p.end_c - seconds_today) % 60:02d}"
                )
                # move terminal cursor UP 2 rows and redraw
                print("\033[2F", end="")
            # Se verifică dacă perechile/pauzele s-au terminat
            elif periods.index(p) == len(periods) - 1 and seconds_today > p.end_c:
                print("IT'S OVEEEEEEEEEEEER")
                sys.exit(0)

        time.sleep(TICK)


if __name__ == "__main__":
    main()
