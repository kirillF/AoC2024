from utils import read_input, solve_part
from collections import defaultdict
from functools import cmp_to_key


def create_order(rules):
    m = defaultdict(set)
    for a, b in rules:
        m[a].add(b)
    return m


def compare(a, b, order):
    return -1 if b not in order or b in order[a] else 0


def is_sorted(page, order):
    return all(compare(page[i], page[i + 1], order) < 0 for i in range(len(page) - 1))


def sort(page, order):
    return sorted(page, key=cmp_to_key(lambda x, y: compare(x, y, order)))


def prepare(data):
    parts = data.split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in parts[0].splitlines()]
    pages = [list(map(int, page.split(","))) for page in parts[1].splitlines()]
    return create_order(rules), pages


def part1(data):
    order, pages = prepare(data)
    return sum(page[len(page) // 2] for page in pages if is_sorted(page, order))


def part2(data):
    order, pages = prepare(data)
    return sum((sort(page, order)[len(page) // 2]) for page in pages if not is_sorted(page, order))


if __name__ == "__main__":
    path = "day5/5.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
