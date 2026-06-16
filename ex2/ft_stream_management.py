#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "<file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")

    source_file = None
    try:
        source_file = open(filename)
        content = source_file.read()
        print("---\n")
        print(content, end="")
        print("\n---")
    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}':", e, file=sys.stderr)
        return
    finally:
        if source_file is not None:
            source_file.close()
            print(f"File '{filename}' closed.")
            print("")

    content_new = "#\n".join(content.split("\n"))
    print("Transform data:")
    print("---\n")
    print(content_new, end="")
    print("\n---")

    print("Enter new file name (or empty): ", end="", flush=True)
    filename_new = sys.stdin.readline().removesuffix("\n")
    if not filename_new:
        print("Not saving data.")
        return

    save_file = None
    try:
        print(f"Saving data to '{filename_new}'")
        save_file = open(filename_new, "w")
        save_file.write(content_new)
        print(f"Data saved in file '{filename_new}'.")
    except OSError as e:
        print(f"[STDERR] Error saving file '{filename_new}':", e)
        return
    finally:
        if save_file is not None:
            save_file.close()


if __name__ == "__main__":
    main()
