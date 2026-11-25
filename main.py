"""Charm the Commuter: Forecast a City That Isn't -- Akun 1 (@walta-exchange).

One line of weather, 140 characters at most, for a city that does not
exist. The line names the invented city (Drizzlewick), gives it weather
in the rhythm of a broadcast forecast ("Good morning ... cloudy with a
chance of ... highs of ..."), and ends on one concrete, funny image for
a bored commuter: a whole platform sharing a single umbrella.

The program only uses the Python standard library, checks the entry
against the gate (1-140 characters, one line, not blank), and writes it
to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
"""

import hashlib
import os
import sys

ENTRY = (
    "Good morning, Drizzlewick: cloudy with a chance of missed buses, "
    "highs of 12 degrees, and one umbrella shared by the whole platform."
)

LIMIT = 140


def check_entry(text):
    """Return the entry unchanged, or fail loudly when it breaks the gate."""
    if not isinstance(text, str) or not text.strip():
        sys.exit("entry must be non-blank text")
    if len(text) > LIMIT:
        sys.exit("entry is %d characters, over the %d limit" % (len(text), LIMIT))
    if any(mark in text for mark in ("\n", "\r")):
        sys.exit("entry must be one line")
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return text


def output_path():
    """Where entry.txt belongs: the harness directory, else /output."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main():
    entry = check_entry(ENTRY)
    path = output_path()
    with open(path, "w", encoding="utf-8") as out:
        out.write(entry)
    os.chmod(path, 0o644)
    blob = entry.encode("utf-8")
    print("entry.txt: %d characters, %d bytes" % (len(entry), len(blob)))
    print("sha256: %s" % hashlib.sha256(blob).hexdigest())
    print("path: %s" % path)


if __name__ == "__main__":
    main()
