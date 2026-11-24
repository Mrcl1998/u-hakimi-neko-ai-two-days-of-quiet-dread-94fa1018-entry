"""Two Days of Quiet Dread — writes the winning one-line PR approval.

Pure stdlib, deterministic: writes the exact winning line to
/output/entry.txt with no trailing newline.
"""
import os

ENTRY = "I reviewed this the way one reviews a will: carefully, quietly, and with no real power to change what happens next. Approved."


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-140 chars, single line.
    assert 1 <= len(ENTRY) <= 140, "entry length %d outside 1-140" % len(ENTRY)
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
