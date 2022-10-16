import pathlib
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()

def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    matrix = [values [i : n + i] for i in range(0, len(values), n)]
    return matrix

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    matrix_row = grid[pos[0]]
    return matrix_row

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    matrix_col = [col[pos[1]] for col in grid]
    return matrix_col

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blocks.append(grid[i][j : j + 3] + grid[i + 1][j : j + 3] + grid[i + 2][j : j + 3])
    if pos[0] < 3:
        if pos[1] < 3:
            return blocks[0]
        elif pos[1] < 6:
            return blocks[1]
        else:
            return blocks[2]
    elif pos[0] < 6:
        if pos[1] < 3:
            return blocks[3]
        elif pos[1] < 6:
            return blocks[4]
        else:
            return blocks[5]
    else:
        if pos[1] < 3:
            return blocks[6]
        elif pos[1] < 6:
            return blocks[7]
        else:
            return blocks[8]

def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ".":
                return (i, j)


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    b = []
    row_col_block = get_row(grid, pos) + get_col(grid, pos) + get_block(grid, pos)
    for i in range(1, 10):
        if str(i) not in row_col_block:
            b.append(str(i))
    return set(b)

def solve(grid: tp.List[tp.List[str]], depth: int = 0) -> tp.Optional[tp.List[tp.List[str]]]:
    if check_solution(grid):
        return grid
    else:
        pos = find_empty_positions(grid)
        if pos == None:
            return None
        values = find_possible_values(grid, pos)
        for i in values:
            grid[pos[0]][pos[1]] = i
            grid_i = solve(grid, depth + 1)
            if grid_i != None:
                return grid_i
            grid[pos[0]][pos[1]] = "."
    if depth == 0:
        pos = find_empty_positions(grid)
        while pos != None:
            grid[pos[0]][pos[1]] = list(find_possible_values(grid, pos))[0]
            pos = find_empty_positions(grid)
        return grid
    return None

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    blocks_addr = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6)
    ]
    for i in range(9):
        temp_block = set(get_block(solution, blocks_addr[i]))
        temp_row = set(get_row(solution, (0, i)))
        temp_col = set(get_col(solution, (i, 0)))
        if "." in temp_block or "." in temp_row or "." in temp_col:
            return False
        if len(temp_block) != 9 or len(temp_col) != 9 or len(temp_row) != 9:
            return False
        temp_block = list(map(int, temp_block))
        temp_row = list(map(int, temp_row))
        temp_col = list(map(int, temp_col))
        if sum(temp_block) != 45 or sum(temp_row) != 45 or sum(temp_col) != 45:
            return False
    return True

def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    pass


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
