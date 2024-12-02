from utils import read_input, solve_part
from collections import deque


def get_safe_and_unsafe(data):
    res = [[], []]
    for line in data.splitlines():
        values = list(map(int, line.split()))
        res[0].append(values) if is_safe(values) else res[1].append(values)
    return res


def is_safe(values):
    diff_sum = 0
    for prev, curr in zip(values, values[1:]):
        new_diff_sum = diff_sum + prev - curr
        if (
            diff_sum * new_diff_sum < 0
            or abs(diff_sum) >= abs(new_diff_sum)
            or abs(diff_sum - new_diff_sum) > 3
        ):
            return False
        diff_sum = new_diff_sum
    return True


def part1(data):
    return len(get_safe_and_unsafe(data)[0])


def part2(data):
    safe, unsafe = get_safe_and_unsafe(data)
    res = len(safe)
    for values in unsafe:
        if any(is_safe(values[:i] + values[i + 1 :]) for i in range(len(values))):
            res += 1
    return res


if __name__ == "__main__":
    path = "day2/2.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
