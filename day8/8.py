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


def part1(data):
    antennas, m, n = sats(data)
    antinodes = set()
    for pairs in antennas.values():
        for a, b in combinations(pairs, 2):
            A, B, x0, y0 = coords_coeff(a, b)

            offsets = [(1.5 * B, 1.5 * A), (-1.5 * B, -1.5 * A)]
            for dx, dy in offsets:
                ax, ay = x0 + dx, y0 + dy
                if 0 <= ax < m and 0 <= ay < n:
                    antinodes.add((ax, ay))

    return len(antinodes)


def part2(data):
    antennas, m, n = sats(data)
    antinodes = set()
    for pairs in antennas.values():
        for a, b in combinations(pairs, 2):
            A, B, x0, y0 = coords_coeff(a, b)

            directions = [(1.5 * B, 1.5 * A), (-1.5 * B, -1.5 * A)]
            for dx, dy in directions:
                x, y = x0 + dx, y0 + dy
                while 0 <= x < m and 0 <= y < n:
                    antinodes.add((x, y))
                    x += dx / 1.5
                    y += dy / 1.5
            antinodes.update({a, b})

    return len(antinodes)


if __name__ == "__main__":
    path = "day8/8.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
