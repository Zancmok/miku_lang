import sys


def main(argv: list[str]) -> None:
    if len(argv) <= 1:
        return

    print(argv)


if __name__ == '__main__':
    main(sys.argv)
