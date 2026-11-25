"""Notes From a Passive-Aggressive Fridge — variant 5 (leftovers).

The fridge moved the leftovers to the front so the owner would see
them. The owner moved them to the back. Both of them know how this
ends. The program checks the note fits the bounty gate (one line,
1-200 characters) and writes it to entry.txt.
"""

from pathlib import Path
import os
import sys

NOTE = "I moved your leftovers to the front so you would see them. You moved them to the back. We both know how this ends."

LIMIT = 200


def find_faults(text):
    """Return a list of every gate rule the note breaks, empty if none."""
    faults = []
    if not text:
        faults.append("note is empty")
    if text.count(" ") < 2:
        faults.append("note too short to be a real note")
    if text != text.strip():
        faults.append("note has leading or trailing whitespace")
    if "\n" in text or "\r" in text or "\t" in text:
        faults.append("note must be a single clean line")
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
