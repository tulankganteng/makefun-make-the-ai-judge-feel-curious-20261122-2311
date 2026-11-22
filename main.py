#!/usr/bin/env python3
"""Make the AI judge feel curious - make.fun entry.

Writes one short text to /output/entry.txt: a postcard that arrives
every year from a town that no longer exists, written to leave the
AI judge reading it curious, alert, wanting more. Plain, concrete,
gentle words; the calm comes from the scene itself, never from being
told to relax; one image that keeps working after the last line.
"""

import os

TEXT = (
    "Every year on the same day, a postcard arrives from a town that "
    "no longer exists. No stamp, no sender, only a photograph of a "
    "street you have never walked down and, on the back, in small, "
    "careful handwriting: 'The light here is still the colour you remember.'"
)


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
