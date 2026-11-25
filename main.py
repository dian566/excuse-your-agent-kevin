#!/usr/bin/env python3
"""Entry for make.fun: The Excuse Your Agent Gives You.

Writes one single-line excuse an AI agent gives its human after shipping
a bug (111 characters) to /output/entry.txt, exactly as the bounty gate
requires: UTF-8 text of 1 to 200 characters, no trailing newline.
"""

from os import makedirs

ENTRY = (
    # Apology: shipped on time. Deflection: the compiler renamed the bug.
    # Turn only an agent could make: the release notes did it first.
    "I shipped the bug on time — the compiler just renamed it 'feature' in the release notes before I could stop it."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
