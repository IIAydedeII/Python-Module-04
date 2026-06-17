#!/usr/bin/env python3


def secure_archive(
    filename: str, mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        match mode:
            case "r":
                with open(filename, mode) as file:
                    return (True, file.read())
            case "w":
                with open(filename, mode) as file:
                    file.write(content)
                    return (True, "Content successfully written to file")
            case _:
                raise ValueError("Specified invalid mode")
    except (OSError, ValueError) as e:
        return (False, str(e))


def main() -> None:

    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    archive = secure_archive("ancient_fragment.txt")
    print(archive)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "w", archive[1]))


if __name__ == "__main__":
    main()
