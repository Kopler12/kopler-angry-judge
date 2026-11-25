"""Write one short, funny rant about an everyday annoyance.

The rant is about autocorrect: a phone that has never once fixed a real
typo, yet happily rewrites "meeting" into "mating" in an email to the boss.
One text, under 400 characters, written to /output/entry.txt. Runs in a
sandbox with no network.
"""

import os

ENTRY = (
    "My phone autocorrected 'meeting' to 'mating' in an email to my boss. "
    "I have now officially invited the client to mate with me at 3 p.m. "
    "Autocorrect has never fixed a single real typo, but it will happily end "
    "your career in one tap, and then suggest I meant 'ducking'."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400  # the gate: /output/entry.txt must be 1 to 400 characters


def main() -> None:
    line = ENTRY.replace("\n", " ").strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
