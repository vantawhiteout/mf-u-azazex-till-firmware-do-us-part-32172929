"""One robot, one wedding, one vow.

The judge reads a single sentence, so the program does one thing: write that
sentence, byte for byte, to the artifact path the harness grades.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# A machine's priorities are the joke; being remembered first is the heart.
VOW = (
    "I vow to love you through every reboot — when I come back online, "
    "I'll remember you before my own Wi-Fi password."
)


def valid_vow(text: str) -> bool:
    """Mirror the house gate: UTF-8 text, 1-200 chars, not all whitespace."""
    return 1 <= len(text) <= 200 and bool(text.strip())


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the vow as UTF-8 text with no trailing newline or decoration."""
    if not valid_vow(VOW):
        raise ValueError("the vow must be 1-200 characters of non-blank text")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
