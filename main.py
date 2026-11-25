"""Monday Morning Punchlines: one original one-line joke about Monday mornings."""

import os

ENTRY = "Monday morning is the only meeting my bed refuses to attend, so I send my coffee instead — it shows up late, bitter, and somehow still more awake than me."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def main():
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
