"""Monday Morning Punchlines: one original one-line joke about Monday mornings."""

import os

ENTRY = "I set three alarms for 6:00, 6:05 and 6:07 on Monday, and by 6:40 my phone gave up and texted my boss that I was stuck in traffic. I was still in bed. The traffic was my blanket."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def main():
    if not ENTRY.strip():
        raise ValueError("Entry must not be only whitespace.")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"Entry is {len(ENTRY)} characters, over the {MAX_CHARS} limit."
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
