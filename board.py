import itertools
from enum import Enum


class State(Enum):
    BLANK = 0
    SHADED = 1
    UNSHADED = 2


class Cell:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        self.state: State = State.BLANK

    def __repr__(self):
        return f'{self.row}, {self.col}: {self.state.name}'

    def get_state_str(self) -> str:
        match self.state:
            case State.BLANK:
                return '□'
            case State.SHADED:
                return '■'
            case State.UNSHADED:
                return 'x'

    def shade(self):
        if self.state != State.BLANK:
            raise NotBlankError(self)
        self.state = State.SHADED

    def unshade(self):
        if self.state != State.BLANK:
            raise NotBlankError(self)
        self.state = State.UNSHADED


class NotBlankError(RuntimeError):
    def __init__(self, cell: Cell):
        super().__init__(f"cell {cell} is not blank")


class Board:
    def __init__(self, row_rules: list[list[int]], col_rules: list[list[int]]):
        self.row_rules: list[list[int]] = row_rules
        self.col_rules: list[list[int]] = col_rules
        self._layout: list[list[Cell]] = [[Cell(row, col) for col in range(len(self.col_rules))] for row in range(len(self.row_rules))]

    def get_rows(self) -> list[list[Cell]]:
        return self._layout

    def get_rows_with_rules(self) -> list[tuple[list[Cell], list[int]]]:
        return list(zip(self.get_rows(), self.row_rules))

    def get_cols(self) -> list[list[Cell]]:
        return [[self._layout[row][col] for row in range(len(self.row_rules))] for col in range(len(self.col_rules))]

    def get_cols_with_rules(self) -> list[tuple[list[Cell], list[int]]]:
        return list(zip(self.get_cols(), self.col_rules))


    def print_board(self):
        print("+", end='')
        print("-" * (len(self.col_rules) * 3 + 2), end='')
        print("+")

        for row in range(len(self.row_rules)):
            print("|  ", end='')
            for col in range(len(self.col_rules)):
                print(self._layout[row][col].get_state_str(), end='')
                print("  ", end='')
            print("| ", end='')
            print(*self.row_rules[row], sep=' ')

        print("+", end='')
        print("-" * (len(self.col_rules) * 3 + 2), end='')
        print("+")

        for line in itertools.zip_longest(*self.col_rules, fillvalue=' '):
            print(" ", end='')
            for num in line:
                print(f"{num:>3}", end='')
            print()


if __name__ == '__main__':
    board = Board([[1, 1], [2], []], [[3], [1, 1], [10]])
    board.get_rows()[0][0].shade()
    board.get_cols()[1][2].unshade()
    try:
        board.get_rows()[0][0].shade()
    except NotBlankError as e:
        print(e)
    board.print_board()

    print()
    print(*board.get_rows(), sep='\n')
    print()
    print(*board.get_cols(), sep='\n')
