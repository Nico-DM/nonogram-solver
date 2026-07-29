from board import Board, Cell, State
from line_solving import solve_line


def main():
    board = Board(
                  [[2], [2,1], [1,1], [3], [1,1], [1,1], [2], [1,1], [1,2], [2]],
                  [[2,1], [2,1,3], [7], [1,3], [2,1]]
                  )

    job_list = board.get_rows_with_rules() + board.get_cols_with_rules()

    step = 0

    while job_list:
        job: tuple[list[Cell], list[int]] = job_list.pop(0)
        changed = solve_line(*job)

        if changed:
            step += 1
            print(f"\nStep {step}:")
            board.print_board()

        while changed:
            changed_cell: Cell = changed.pop()

            changed_row: tuple[list[Cell], list[int]] = board.get_rows_with_rules()[changed_cell.row]
            if changed_row not in job_list and changed_row != job:
                job_list.append(changed_row)

            changed_col: tuple[list[Cell], list[int]] = board.get_cols_with_rules()[changed_cell.col]
            if changed_col not in job_list and changed_col != job:
                job_list.append(changed_col)

    for row in board.get_rows():
        for cell in row:
            if cell.state == State.BLANK:
                cell.unshade()

    print("\nSolution:")
    board.print_board()


if __name__ == "__main__":
    main()