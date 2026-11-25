"""Notes From a Passive-Aggressive Fridge — variant 1 (milk).

The fridge kept the expired milk on purpose: somebody in this house
ought to remember things, and the owner clearly does not. The program
checks the note fits the bounty gate (one line, 1-200 characters) and
writes it to entry.txt.
"""

from pathlib import Path
import os
import sys

NOTE = "Your milk expired Tuesday. I kept it anyway — someone in this house should remember something, and it clearly isn't you."

LIMIT = 200


def find_faults(text):
    """Return a list of every gate rule the note breaks, empty if none."""
    faults = []
    if text != text.strip():
        faults.append("note has leading or trailing whitespace")
    if len(text) < 1 or len(text) > LIMIT:
        faults.append("length outside 1-200 characters")
    if "\n" in text or "\r" in text:
        faults.append("note must be a single line")
    return faults


def main():
    faults = find_faults(NOTE)
    if faults:
        print("invalid note: " + "; ".join(faults), file=sys.stderr)
        return 1
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(NOTE, encoding="utf-8")
    if target.read_text(encoding="utf-8") != NOTE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d characters)" % (target, len(NOTE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
