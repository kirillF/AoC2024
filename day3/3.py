from utils import read_input, solve_part
import re


def process(data):
    return sum(int(a) * int(b) for a, b in re.findall(r"(?:mul\()(\d{1,3}),(\d{1,3})(?=\))", data))


def part1(data):
    return process(data)


def part2(data):
    return sum(process(do) for do in re.findall(r"(?:^|do\(\))(.*?)(?=don't\(\)|$)", data.replace("\n", "")))


if __name__ == "__main__":
    path = "day3/3.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
