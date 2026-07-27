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

    def __str__(self):
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
    def __init__(self, rows: int, cols: int, row_rules: list[list[int]], col_rules: list[list[int]]):
        self.rows: int = rows
        self.cols: int = cols
        self.row_rules: list[list[int]] = row_rules
        self.col_rules: list[list[int]] = col_rules
        self.layout: list[list[Cell]] = [[Cell(row, col) for col in range(self.cols)] for row in range(self.rows)]

    def __str__(self):
        return f'{self.rows} x {self.cols}'

    def print_board(self):
        print("+", end='')
        print("-" * (self.cols * 2 + 1), end='')
        print("+")

        for row in range(self.rows):
            print("| ", end='')
            for col in range(self.cols):
                print(self.layout[row][col].get_state_str(), end='')
                print(" ", end='')
            print("| ", end='')
            print(*self.row_rules[row], sep=' ')

        print("+", end='')
        print("-" * (self.cols * 2 + 1), end='')
        print("+")

        for line in itertools.zip_longest(*self.col_rules, fillvalue=' '):
            print(*line, sep=' ')


if __name__ == '__main__':
    board = Board(3, 3, [[1, 1], [2], []], [[], [1, 1], [3]])
    board.layout[0][0].shade()
    board.layout[1][1].unshade()
    try:
        board.layout[0][0].shade()
    except NotBlankError as e:
        print(e)
    board.print_board()
