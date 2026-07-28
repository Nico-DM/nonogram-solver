from board import Cell, Board


def fill_line(row: list[Cell], row_rule: list[int]) -> bool:
    changed: bool = False
    total: int = sum(row_rule) + len(row_rule) - 1
    if total != len(row):
        return changed

    cell_num = 0
    for clue in row_rule:
        i = 0
        while i < clue:
            changed = True
            row[cell_num].shade()
            i += 1
            cell_num += 1
        if clue != row_rule[-1]:
            changed = True
            row[cell_num].unshade()
            cell_num += 1

    return changed


def box_overlap(row: list[Cell], row_rule: list[int]) -> bool:
    changed: bool = False
    start_crowd: list[int | None] = [None for _ in row]

    cell_num = 0
    for clue in row_rule:
        i = 0
        while i < clue:
            start_crowd[cell_num] = clue
            i += 1
            cell_num += 1
        cell_num += 1

    leftover: int = len(row) - cell_num + 1
    end_crowd: list[int | None] = [None for _ in row]

    cell_num = leftover
    for clue in row_rule:
        i = 0
        while i < clue:
            end_crowd[cell_num] = clue
            i += 1
            cell_num += 1
        cell_num += 1

    for pos in range(len(row)):
        if start_crowd[pos] is not None and end_crowd[pos] is not None and start_crowd[pos] == end_crowd[pos]:
            changed = True
            row[pos].shade()

    return changed


if __name__ == '__main__':
    board = Board(2, 10, [[4,3,1], [4,3]], [])
    print(f"Row 0 (fill_line): {fill_line(board.get_rows()[0], board.row_rules[0])}")
    print(f"Row 1 (box_overlap): {box_overlap(board.get_rows()[1], board.row_rules[1])}")
    board.print_board()
