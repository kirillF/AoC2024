from utils import read_input, solve_part, data_to_matrix
from collections import defaultdict


def dfs(matrix, visited, item, i, j, m, n):
    stack = [(i, j)]
    res = 0
    pp = 0
    borders = []

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        res += 1

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == item:
                if not visited[nx][ny]:
                    stack.append((nx, ny))
            else:
                borders.append(((nx, ny), (dx, dy)))
                pp += 1

    return res, pp, borders


def part1(data):
    matrix = data_to_matrix(data)
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]

    maps = defaultdict(tuple)
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                maps[(i, j)] = dfs(matrix, visited, matrix[i][j], i, j, m, n)

    return sum(v[0] * v[1] for v in maps.values())


def part2(data):
    matrix = data_to_matrix(data)
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]

    res = 0
    p = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                r, pp, borders = dfs(matrix, visited, matrix[i][j], i, j, m, n)
                res += r
                s = set(borders)
                for border in borders:
                    dx, dy = border[1]
                    x, y = border[0]
                    if ((x - dy, y + dx), (dx, dy)) in s:
                        pp -= 0.5
                    if ((x + dy, y - dx), (dx, dy)) in s:
                        pp -= 0.5
                p += int(pp) * r

    return p


if __name__ == "__main__":
    path = "day12/12.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
