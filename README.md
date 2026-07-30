# nonogram-solver

A simple Python nonogram (picross) solver built as a personal project for [Boot.dev](https://www.boot.dev).

The solver works line by line: for each row or column it finds every placement that still fits the clues and the cells already marked, then marks cells that are the same in every valid placement. When a cell changes, the corresponding row and column are queued again until nothing new can be deduced.

It can only handle puzzles designed to be line-solved (i.e. with the left-right overlap technique), and up to ~25x25 in size.

## Requirements

- Python 3.12+

## Usage

Run the solver with a puzzle file:

```bash
python main.py examples/dancer.txt
```

If no file is given, `examples/dancer.txt` is used by default.

The solver prints each deduction step and the final solution. Cells are shown as:

| Symbol | Meaning   |
|--------|-----------|
| `□`    | Unknown   |
| `■`    | Filled    |
| `.`    | Empty     |

## Puzzle file format

Puzzle files are plain text with two sections separated by a blank line:

1. **Row clues** — one row per line, space-separated block lengths (top to bottom)
2. **Column clues** — one row per line, space-separated block lengths (left to right)

Example (`examples/cat.txt`):

```
2
2
1 1
...

5
5 3
2 3 4
...
```

An empty clue list is represented with a lone `0` (like in `skid.txt`).

## Project structure

| File              | Description                                       |
|-------------------|---------------------------------------------------|
| `main.py`         | Entry point; runs the solve loop and prints steps |
| `parser.py`       | Reads puzzle files into row and column clue lists |
| `board.py`        | Grid, cell states, and board rendering            |
| `line_solving.py` | Line solver: backtracking, intersection, updates  |
| `examples/`       | Sample puzzles                                    |

## How it works

1. **Parse** the puzzle into row and column clue lists and build an empty board.
2. **Queue** every row and column for processing.
3. For each line, **generate** all valid fill patterns that match the clues and fixed cells (backtracking).
4. **Intersect** those patterns: cells that are filled or empty in every pattern are marked on the board.
5. When a cell changes, **re-queue** that row and column.
6. Repeat until the queue is empty, then mark any remaining unknown cells as empty.

## Examples

Several puzzles are included in `examples/`:

- `dancer.txt` (10 x 5)
- `cat.txt` (20 x 20)
- `skid.txt` (25 x 14)
- `knot.txt` (34 x 34) - this one takes a bit

> Copyright 2004 by Jan Wolter from [webpbn.com](https://webpbn.com)

## License

MIT (see [LICENSE](LICENSE))
