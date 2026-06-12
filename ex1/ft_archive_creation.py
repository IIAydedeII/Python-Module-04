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
        source_file = open(filename)
    except OSError as e:
        print(f"Error opening file '{filename}':", e)
        return

    content = source_file.read()

    print("---\n")
    print(content, end="")
    print("\n---")

    source_file.close()
    print(f"File '{filename}' closed.")
    print("")

    content_new = "#\n".join(content.split("\n"))
    print("Transform data:")
    print("---\n")
    print(content_new, end="")
    print("\n---")

    filename_new = input("Enter new file name (or empty): ")

    if not filename_new:
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{filename_new}'")
        save_file = open(filename_new, "w")
    except OSError as e:
        print(f"Error saving file '{filename}':", e)
        return

    save_file.write(content_new)
    print(f"Data saved in file '{filename_new}'.")
    save_file.close()


if __name__ == "__main__":
    main()
