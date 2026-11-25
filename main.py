"""One-line office joke entry for the make.fun bounty.

Writes a single original one-line office joke (1-199 characters) to
``entry.txt`` inside ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Standard library only, no network access, fully deterministic: the same
ENTRY is written on every run.
"""

import os

ENTRY = (
    "Our printer only jams when the CEO visits, so I have started "
    "introducing it to new hires as the office's most reliable "
    "early-warning system."
)

assert 1 <= len(ENTRY) <= 199, "ENTRY must be 1-199 characters"
assert "\n" not in ENTRY, "ENTRY must be a single line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
