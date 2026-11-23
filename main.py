#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast line to /output/entry.txt.

Deterministic, offline, stdlib-only. The roast is a fixed string literal:
the program always writes exactly the same bytes.

Candidate lines considered (brainstormed, then cut to the one that lands
hardest): the agent billing me for the roast, the agent apologising in
bullets, the agent planning for six hours then asking if it was funny.
The chosen line won because it has a short setup, a fresh angle (the
agent dodging its own roast by delegating it back to me), and the
punchline lands on the last word.
"""

import os

ROAST = (
    "I asked my agent to roast itself \u2014 it outsourced the joke "
    "to me and called it collaboration."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
