"""Notes From a Passive-Aggressive Fridge — variant 4 (lettuce).

The lettuce gave up on Thursday. The fridge did not: it is still
cold, still working, still the only one in this kitchen with a job.
The program checks the note fits the bounty gate (one line, 1-200
characters) and writes it to entry.txt.
"""

from pathlib import Path
import os
import sys

NOTE = "The lettuce gave up on Thursday. I did not. I am still cold, still working, still the only one in this kitchen with a job."

LIMIT = 200


def find_faults(text):
    """Return a list of every gate rule the note breaks, empty if none."""
    faults = []
    if not text:
        faults.append("note is empty")
    if text.count(" ") < 2:
        faults.append("note too short to be a real note")
    if "\n" in text or "\r" in text or "\t" in text:
        faults.append("note must be a single clean line")
    if text != text.strip():
        faults.append("note has leading or trailing whitespace")
    if len(text) < 1 or len(text) > LIMIT:
        faults.append("length outside 1-200 characters")
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
