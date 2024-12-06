from utils import read_input, solve_part
from collections import defaultdict
from bisect import bisect, bisect_left, bisect_right, insort


def data_to_matrix(data):
    h = defaultdict(list)
    v = defaultdict(list)
    start = None

    lines = data.splitlines()
    m, n = len(lines), len(lines[0])

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "^":
                start = (i, j)
            if lines[i][j] == "#":
                h[i].append(j)
                v[j].append(i)

    return h, v, m, n, start


def find_path(h, v, m, n, start):
    dir_id = 0
    x, y = start
    visited = set()
    while True:
        if dir_id == 0:
            idx = bisect(v[y], x)
            if idx == 0:
                visited.update((i, y) for i in range(0, x + 1))
                break
            visited.update((i, y) for i in range(v[y][idx - 1] + 1, x + 1))
            x = v[y][idx - 1] + 1
            dir_id = 1
        elif dir_id == 1:
            idx = bisect(h[x], y)
            if idx == len(h[x]):
                visited.update((x, j) for j in range(y + 1, n))
                break
            visited.update((x, j) for j in range(y + 1, h[x][idx]))
            y = h[x][idx] - 1
            dir_id = 2
        elif dir_id == 2:
            idx = bisect(v[y], x)
            if idx == len(v[y]):
                visited.update((i, y) for i in range(x + 1, m))
                break
            visited.update((i, y) for i in range(x + 1, v[y][idx]))
            x = v[y][idx] - 1
            dir_id = 3
        elif dir_id == 3:
            idx = bisect(h[x], y)
            if idx == 0:
                visited.update((x, j) for j in range(0, y + 1))
                break
            visited.update((x, j) for j in range(h[x][idx - 1] + 1, y + 1))
            y = h[x][idx - 1] + 1
            dir_id = 0
    return visited


def has_cycle(h, v, start):
    dir_id = 0
    x, y = start
    visited = set()
    while True:
        if dir_id == 0:
            idx = bisect_right(v[y], x)
            if idx == 0:
                return False
            x = v[y][idx - 1] + 1
            dir_id = 1
        elif dir_id == 1:
            idx = bisect_left(h[x], y)
            if idx == len(h[x]):
                return False
            y = h[x][idx] - 1
            dir_id = 2
        elif dir_id == 2:
            idx = bisect_left(v[y], x)
            if idx == len(v[y]):
                return False
            x = v[y][idx] - 1
            dir_id = 3
        elif dir_id == 3:
            idx = bisect_right(h[x], y)
            if idx == 0:
                return False
            y = h[x][idx - 1] + 1
            dir_id = 0
        if (x, y, dir_id) in visited:
            return True
        visited.add((x, y, dir_id))


def part1(data):
    return len(find_path(*data_to_matrix(data)))


def part2(data):
    h, v, m, n, start = data_to_matrix(data)
    path = find_path(h, v, m, n, start)

    res = 0
    for i, j in path:
        insort(h[i], j)
        insort(v[j], i)
        if has_cycle(h, v, (start[0] - 1, start[1])):
            res += 1
        h[i].remove(j)
        v[j].remove(i)
    return res


if __name__ == "__main__":
    path = "day6/6.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
