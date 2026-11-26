"""Write the patch note announcing that human sleep has been fixed."""

import os

LINE = "Resolved: the 3 AM replay of every embarrassing thing since 2009 has been moved to business hours."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
