from board import Cell, State


def generate_line_solutions(cells: list[Cell], clues: list[int]) -> list[list[State]]:
    solutions: list[list[State]] = []

    def follows_clues(line: list[State]) -> bool:
        test_line = [State.SHADED if state == State.SHADED or cell.state == State.SHADED else State.UNSHADED for state, cell in zip(line, cells)]
        pos = 0

        for clue in clues:
            while test_line[pos] == State.UNSHADED:
                pos += 1
            for i in range(clue):
                if test_line[pos] != State.SHADED:
                    return False
                test_line.pop(pos)

        return all(state == State.UNSHADED for state in test_line)


    def can_place(line: list[State], pos: int, size: int) -> bool:
        start, end = pos, pos + size

        if len(line) < pos + size:
            return False

        if any([cell.state == State.UNSHADED for cell in cells[start:end]]):
            return False

        if end < len(cells) - 1 and cells[end].state == State.SHADED:
            return False

        if start != 0 and cells[start - 1].state == State.SHADED:
            return False

        return True

    def place_block(line: list[State], pos: int, size: int) -> list[State]:
        new_line: list[State] = line[:]
        for idx in range(pos, pos + size):
            new_line[idx] = State.SHADED

        return new_line

    def backtrack(clue_idx: int, start: int, line: list[State]):
        if clue_idx == len(clues):
            if follows_clues(line):
                solutions.append(line)
            return

        size = clues[clue_idx]

        end = len(line) - size - (sum(clues[clue_idx + 1:]) + len(clues[clue_idx + 1:]) - 1)

        for pos in range(start, end):
            if can_place(line, pos, size):
                new_line = place_block(line, pos, size)
                backtrack(clue_idx + 1, pos + size + 1, new_line)

    backtrack(0, 0, [State.UNSHADED] * len(cells))
    return solutions


def intersect_solutions(solutions: list[list[State]]) -> list[State]:
    new_states: list[State] = [State.BLANK] * len(solutions[0])

    for pos in range(len(solutions[0])):
        state: State = solutions[0][pos]
        if all(solution[pos] == state for solution in solutions):
            new_states[pos] = state

    return new_states


def update(cells: list[Cell], new_states: list[State]) -> list[Cell]:
    updated_cells: list[Cell] = []

    for cell, state in zip(cells, new_states):
        if cell.state == State.BLANK:
            if state == State.SHADED:
                cell.shade()
                updated_cells.append(cell)
            if state == State.UNSHADED:
                cell.unshade()
                updated_cells.append(cell)

    return updated_cells


def solve_line(cells: list[Cell], clues: list[int]) -> list[Cell]:
    if not clues or clues == [0]:
        return update(cells, [State.UNSHADED] * len(cells))
    solutions = generate_line_solutions(cells, clues)
    if solutions:
        new_states = intersect_solutions(solutions)
        return update(cells, new_states)
    return []
