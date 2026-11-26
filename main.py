"""Write this entry's one-line lost sock status update to entry.txt."""

import os

ENTRY = "Day 47 behind the dryer. I have started a new life with a lint ball and I am not coming home for Christmas."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
