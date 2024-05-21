import sys

from Interpreter import Interpreter


def main(argv: list[str]) -> None:
    if len(argv) <= 1:
        return

    file_content: str

    with open(argv[1]) as file:
        file_content = file.read()

    interpreter: Interpreter = Interpreter()

    interpreter.interpret(file_content)


if __name__ == '__main__':
    main(sys.argv)
