from utils import read_input, solve_part
from functools import lru_cache


def solve(data, steps):
    nums = list(map(int, data.split()))

    @lru_cache(None)
    def process_num(k, step):
        if step == 0:
            return 1

        if k == 0:
            return process_num(1, step - 1)

        else:
            k_str = str(k)
            if len(k_str) % 2 == 0:
                mid = len(k_str) // 2
                k_1 = int(k_str[:mid])
                k_2 = int(k_str[mid:])
                return process_num(k_1, step - 1) + process_num(k_2, step - 1)
            else:
                return process_num(k * 2024, step - 1)

    return sum(process_num(num, steps) for num in nums)


def part1(data):
    return solve(data, 25)


def part2(data):
    return solve(data, 75)


if __name__ == "__main__":
    path = "day11/11.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
