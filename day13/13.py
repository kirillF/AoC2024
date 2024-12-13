from utils import read_input, lines_to_pairs, execution_time, solve_part
from collections import defaultdict
import re


def coeffs(data):
    regex = re.compile(r"(?:\+|=)(\d+).+?(?:\+|=)(\d+)")
    for eq in data.split("\n\n"):
        yield [tuple(map(int, regex.findall(line)[0])) for line in eq.split("\n")]


def solve_eq(coeffs, extend=0):
    a, b, c = coeffs
    c0, c1 = extend + c[0], extend + c[1]
    denominator = a[0] * b[1] - a[1] * b[0]
    x = (c0 * b[1] - c1 * b[0]) / denominator
    y = (a[0] * c1 - a[1] * c0) / denominator
    return x, y


def solve(data, extend=0):
    return int(
        sum(
            3 * x + y
            for x, y in map(lambda coeffs: solve_eq(coeffs, extend), coeffs(data))
            if x.is_integer() and y.is_integer()
        )
    )


def part1(data):
    return solve(data)


def part2(data):
    return solve(data, 10000000000000)


if __name__ == "__main__":
    path = "day13/13.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
