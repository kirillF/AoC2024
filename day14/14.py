import curses
from utils import read_input, lines_to_pairs, execution_time, solve_part
from collections import defaultdict
import re
from functools import reduce


def robots(data):
    pattern = re.compile(r"p=(\d+),(\d+) v=(-?\d+),*(-?\d+)")
    for line in data.splitlines():
        x, y, vx, vy = map(int, pattern.match(line).groups())
        yield ((x, y), (vx, vy))


def part1(data):
    m, n = 101, 103
    mid_x, mid_y = m // 2, n // 2
    res = [0, 0, 0, 0]
    for o in robots(data):
        x, y = (o[0][0] + o[1][0] * 100) % m, (o[0][1] + o[1][1] * 100) % n
        if x < mid_x and y < mid_y:
            res[0] += 1
        if x > mid_x and y < mid_y:
            res[1] += 1
        if x > mid_x and y > mid_y:
            res[2] += 1
        if x < mid_x and y > mid_y:
            res[3] += 1
    return reduce(lambda acc, x: acc * x, res, 1)


def draw(stdscr, data):
    m, n = 101, 103
    curses.resize_term(n + 2, m + 1)
    for i in range(0, 10000):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Time: {i}")
        matrix = [["."] * m for _ in range(n)]
        for o in robots(data):
            x, y = (o[0][0] + o[1][0] * i) % m, (o[0][1] + o[1][1] * i) % n
            matrix[y][x] = "#"
        for idx, row in enumerate(matrix):
            stdscr.addstr(1 + idx, 0, "".join(row) + "\n")
        stdscr.refresh()
        stdscr.getch()


def part2(data):
    curses.wrapper(draw, data)


if __name__ == "__main__":
    path = "day14/14.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
