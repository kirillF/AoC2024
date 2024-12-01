from utils import read_input, lines_to_pairs, execution_time, solve_part
import heapq
from collections import defaultdict


def part1(data):
    left, right = [], []

    for a, b in lines_to_pairs(data):
        heapq.heappush(left, a)
        heapq.heappush(right, b)

    return sum(
        abs(heapq.heappop(left) - heapq.heappop(right)) for _ in range(len(left))
    )


def part2(data):
    right = defaultdict(int)
    left = []

    for a, b in lines_to_pairs(data):
        left.append(a)
        right[b] += 1

    return sum(l * right[l] for l in left)


if __name__ == "__main__":
    data = read_input("day1/1.txt")
    solve_part(part1, data)
    solve_part(part2, data)
