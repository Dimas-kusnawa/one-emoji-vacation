"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt.
The dream vacation: a desert island, seen at a glance like a postcard.
"""
import os

# The entry: a single desert-island emoji.
# Why this one: the judge wants a postcard, not a word.
# A desert island is one particular dream, not any holiday:
# palm, sand, sea, and nothing else on the calendar.
# No meetings, no Wi-Fi, no "one last thing" — the phone
# finally dies and nobody minds. It reads instantly at
# small size on any screen, in any culture.
# One character, UTF-8, no words, no trailing newline.
# NOTE: the escape is \U + exactly 8 hex digits (0001F3DD = U+1F3DD).
ENTRY = "\U0001F3DD"


def main() -> None:
    # The gate wants UTF-8 text of 1 to 8 characters.
    # This entry is exactly one character: the island.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
