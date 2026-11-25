"""The Robot Apology - entry for make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes one two-line robot confession to /output/entry.txt:
line 1 apologises for one specific, concrete mistake - replying-all to
the whole office with a birthday message meant for one person - and
line 2 says what the robot learned and what it will do differently.

Standard library only. Deterministic: the same bytes every run.
No network, no randomness, no file reads outside this repository.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm sorry I replied-all to the whole office with the birthday message "
    "you meant only for Mara.\n"
    "I learned a draft is not a send button, so now I read the recipient "
    "list aloud before I let any message go.\n"
)

OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
