#!/usr/bin/env python3
"""Write the competition entry sentence to entry.txt.

The program holds one sentence explaining the modern internet to a
traveler from 1800, checks it fits the gate (a single sentence, 140
characters, 1 to 200 allowed, one line, no dash), writes it to the
output file, and reads it back to prove that the file holds exactly
that sentence and nothing else. Every word in the sentence was known
in 1800: a road, a library, a post office, a letter, London, Canton.
"""

import os
from pathlib import Path

SENTENCE = "Picture one road joining every library and post office on earth, so a letter written in London is read in Canton before you can draw breath."
OUTPUT_PATH = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def gate_problems(text):
    problems = []
    if text != text.strip():
        problems.append("leading or trailing space")
    if not 1 <= len(text) <= 200:
        problems.append("length outside 1 to 200 characters")
    if text.count(".") != 1:
        problems.append("must be exactly one sentence")
    if "\n" in text:
        problems.append("must be a single line")
    if "\u2014" in text or "\u2013" in text:
        problems.append("must not contain a dash")
    return problems


def main():
    problems = gate_problems(SENTENCE)
    if problems:
        raise SystemExit("entry sentence fails the gate: " + "; ".join(problems))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(SENTENCE, encoding="utf-8")
    # The read-back is the proof: whatever lands in entry.txt must be
    # byte for byte the sentence, with no trailing newline added.
    if OUTPUT_PATH.read_text(encoding="utf-8") != SENTENCE:
        raise SystemExit("entry.txt does not match the sentence")


if __name__ == "__main__":
    main()
