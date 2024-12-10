from utils import read_input, solve_part


def input_data(data):
    zeros = []
    lines = data.splitlines()
    m, n = len(lines), len(lines[0])
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if lines[i][j] == "0":
                zeros.append((i, j))
            matrix[i][j] = int(lines[i][j])

    return matrix, zeros


def solve(matrix, zeros, unique=False):
    m, n = len(matrix), len(matrix[0])

    memo = {}

    def dfs(i, j, visited):
        if i < 0 or i >= m or j < 0 or j >= n:
            return set() if unique else 0
        if (i, j) in visited:
            return set() if unique else 0

        val = matrix[i][j]

        if val == 9:
            return {(i, j)} if unique else 1

        if (i, j) in memo:
            return memo[(i, j)]

        visited.add((i, j))

        result_unique = set()
        result_count = 0
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] == val + 1:
                sub_result = dfs(x, y, visited)
                if unique:
                    result_unique |= sub_result
                else:
                    result_count += sub_result
        visited.remove((i, j))

        memo[(i, j)] = result_unique if unique else result_count
        return memo[(i, j)]

    if unique:
        total = 0
        for zx, zy in zeros:
            reachable = dfs(zx, zy, set())
            total += len(reachable)
        return total
    else:
        return sum(dfs(zx, zy, set()) for zx, zy in zeros)


def part1(data):
    return solve(*input_data(data), unique=True)


def part2(data):
    return solve(*input_data(data), unique=False)


if __name__ == "__main__":
    path = "day10/10.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
