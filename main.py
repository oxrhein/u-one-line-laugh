"""One Line, One Laugh — make.fun entry.

Writes a single original one-line joke to entry.txt in the output
directory the grader provides ($MAKEFUN_OUTPUT_DIR, falling back
to /output). Standard library only, no network, fully deterministic.
"""

import os

JOKE = "My AI wrote my apology so well, even I believed I was sorry."

MAX_CHARS = 140


def main():
    line = JOKE.strip()
    assert line, "the joke must not be empty"
    assert "\n" not in line, "the joke must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"the joke must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.strip(), "the joke must not be only whitespace"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)

    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
