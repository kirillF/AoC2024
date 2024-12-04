from utils import read_input, solve_part


def is_match(matrix, i, j, m, n):
    if matrix[i][j] != "X":
        return 0
    letters = ["M", "A", "S"]
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    res = 0
    for dx, dy in dirs:
        x, y = i, j
        found = True
        for k in range(3):
            x += dx
            y += dy
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] != letters[k]:
                found = False
                break
        if found:
            res += 1
    return res


def is_match2(matrix, i, j, m, n):
    if matrix[i][j] != "A":
        return 0
    x, y = i, j
    diags = (((-1, -1), (1, 1)), ((1, -1), (-1, 1)))
    for diag in diags:
        letters = {"M": 1, "S": 1}
        for dx, dy in diag:
            x = i + dx
            y = j + dy
            if (
                x < 0
                or x >= m
                or y < 0
                or y >= n
                or matrix[x][y] not in letters
                or letters[matrix[x][y]] == 0
            ):
                return 0
            letters[matrix[x][y]] = 0
    return 1


def process_input(data, handler):
    matrix = [list(line) for line in data.splitlines()]
    m, n = len(matrix), len(matrix[0])
    return sum(handler(matrix, i, j, m, n) for i in range(m) for j in range(n))


def part1(data):
    return process_input(data, is_match)


def part2(data):
    return process_input(data, is_match2)


if __name__ == "__main__":
    path = "day4/4.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
