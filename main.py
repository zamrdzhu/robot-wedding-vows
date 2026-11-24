"""One line of wedding vows for a robot couple.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The vows keep the classic cadence — sickness and health, till
death do us part — and swap in the robot equivalents: low battery,
airplane mode, and the factory reset that ends a marriage.
"""

import os
import sys

LINE = (
    "I promise to love you in sickness and in health, in low "
    "battery and in airplane mode, until death — or a factory "
    "reset — do us part."
)


def main() -> int:
    if not 1 <= len(LINE) <= 160:
        print(f"error: line is {len(LINE)} chars, must be 1-160",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
