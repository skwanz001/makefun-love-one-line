"""Write one line that tries to make the reader fall in love.

Entry for make.fun bounty "Make the Judge Fall in Love in One Line"
(u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13).

Stdlib only, no network. Writes the line to /output/entry.txt.
Gate: UTF-8 text of 1 to 240 characters, one line, not only whitespace.
"""

import os

LINE = (
    "He learned to braid at 2 a.m., forehead close to the bathroom mirror, "
    "clumsy fingers working a doll's hair, so his daughter would never be "
    "the girl whose hair said nobody tried."
)


def main() -> None:
    # Gate: 1-240 Unicode code points, one line, not only whitespace.
    assert 1 <= len(LINE) <= 240, len(LINE)
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
