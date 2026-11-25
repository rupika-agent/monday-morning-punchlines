"""Monday Morning Punchlines: one joke about Monday mornings.

The script keeps a single joke, checks it against the competition
gate (plain text, between 1 and 200 characters), writes it to
/output/entry.txt, and prints the joke with its character count.
"""

from pathlib import Path

JOKE = "Monday: my 6:00, 6:12 and 6:20 alarms all lost to snooze, so by 6:55 my phone emailed Dave that traffic was gridlocked. I hadn't left bed. The gridlock was my duvet."

CHAR_LIMIT = 200
DESTINATION = Path("/output/entry.txt")


def _checked_text(text):
    """Return the joke unchanged if it passes the gate, else raise."""
    if not text.strip():
        raise ValueError("joke must contain non-whitespace text")
    if len(text) > CHAR_LIMIT:
        raise ValueError(
            "joke is %d characters, over the %d limit" % (len(text), CHAR_LIMIT)
        )
    return text


def _publish(text):
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text + "\n", encoding="utf-8")


def run():
    joke = _checked_text(JOKE)
    _publish(joke)
    print(joke)
    print("chars: %d / %d" % (len(joke), CHAR_LIMIT))


if __name__ == "__main__":
    run()
