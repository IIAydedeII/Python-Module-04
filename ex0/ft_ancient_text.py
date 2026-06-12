#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "<file>")
        return

    print("=== Cyber Archives Recovery ===")

    filename = sys.argv[1]

    print(f"Accessing file '{filename}'")
    try:
        file = open(filename)
    except OSError as e:
        print(f"Error opening file '{filename}':", e)
        return

    print("---\n")
    print(file.read(), end="")
    print("\n---")

    file.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
