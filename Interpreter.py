from Token import Token


class Interpreter:
    def __init__(self) -> None:
        self.code: str = ""

    def _remove_comments(self) -> None:
        new: str = ""

        for line in self.code.split('\n'):
            line_location: int = line.find("//")

            if line_location >= 0:
                line = line[:line_location]

            new += line + '\n'

        self.code = new

    def tokenize(self) -> list[Token]:
        out: list[Token] = []

        for line in self.code.split(';'):
            print(line)

        return out

    def interpret(self, code: str) -> None:
        self.code = code

        self._remove_comments()

        tokens: list[Token] = self.tokenize()


