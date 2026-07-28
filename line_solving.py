from board import Cell, Board


def is_between_same_blocks(cell_pos: int, start_crowd: list[int | None], end_crowd: list[int | None]) -> bool:
    start_right_neighbor = None
    for i in range(cell_pos + 1, len(start_crowd)):
        if start_crowd[i] is not None:
            start_right_neighbor = start_crowd[i]
            break

    end_right_neighbor = None
    for i in range(cell_pos + 1, len(end_crowd)):
        if end_crowd[i] is not None:
            end_right_neighbor = end_crowd[i]
            break

    if start_right_neighbor is not None and end_right_neighbor is not None and start_right_neighbor != end_right_neighbor:
        return False

    start_left_neighbor = None
    for i in range(cell_pos - 1, 0, -1):
        if start_crowd[i] is not None:
            start_left_neighbor = start_crowd[i]
            break

    end_left_neighbor = None
    for i in range(cell_pos - 1, 0, -1):
        if end_crowd[i] is not None:
            end_left_neighbor = end_crowd[i]
            break

    return start_left_neighbor is not None and end_left_neighbor is not None and start_left_neighbor == end_left_neighbor


def line_solving(row: list[Cell], row_rule: list[int]) -> bool:
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
        if start_crowd[pos] is None and end_crowd[pos] is None and is_between_same_blocks(pos, start_crowd, end_crowd):
            changed = True
            row[pos].unshade()

    return changed


if __name__ == '__main__':
    board = Board(2, 10, [[4,3,1], [4,3]], [])
    print(f"Row 0 (full): {line_solving(board.get_rows()[0], board.row_rules[0])}")
    print(f"Row 1 (not full): {line_solving(board.get_rows()[1], board.row_rules[1])}")
    board.print_board()
