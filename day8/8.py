from utils import read_input, solve_part
from collections import defaultdict
from itertools import combinations


def sats(data):
    d = defaultdict(list)
    lines = data.splitlines()
    m = len(lines)
    n = len(lines[0])
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c.isalnum():
                d[c].append((i, j))
    return d, m, n


def coords_coeff(a, b):
    return a[1] - b[1], a[0] - b[0], (a[0] + b[0]) / 2, (a[1] + b[1]) / 2


def solve(map, m, n, extend=False):
    s = set()
    for pairs in map.values():
        for a, b in combinations(pairs, 2):
            A, B, x0, y0 = coords_coeff(a, b)

            dirs = [(1.5 * B, 1.5 * A), (-1.5 * B, -1.5 * A)]
            for dx, dy in dirs:
                x, y = x0 + dx, y0 + dy
                while 0 <= x < m and 0 <= y < n:
                    s.add((x, y))
                    if not extend:
                        break
                    x += dx / 1.5
                    y += dy / 1.5
            if extend:
                s.update({a, b})
    return len(s)


def part1(data):
    s, m, n = sats(data)
    return solve(s, m, n, extend=False)


def part2(data):
    s, m, n = sats(data)
    return solve(s, m, n, extend=True)


if __name__ == "__main__":
    path = "day8/8.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
