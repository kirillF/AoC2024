from utils import read_input, lines_to_pairs, execution_time, solve_part
from collections import defaultdict, deque
from bisect import bisect_left, insort


def part1(data):
    m = len(data)
    arr = []
    for i in range(m):
        arr.append(int(data[i]))
    max_id = m // 2
    l, r = 1, max_id * 2
    res = 0
    id = max_id
    s = arr[0]
    while l <= r:
        if l % 2 == 0:
            idx = l // 2
            sa = arr[l] * (2 * s + arr[l] - 1) // 2
            res += sa * idx
            s += arr[l]
            l += 1
        else:
            if arr[l] == arr[r]:
                sa = arr[l] * (2 * s + arr[l] - 1) // 2
                res += sa * id
                s += arr[l]
                l += 1
                r -= 2
                id -= 1
            elif arr[l] < arr[r]:
                sa = arr[l] * (2 * s + arr[l] - 1) // 2
                res += sa * id
                arr[r] -= arr[l]
                s += arr[l]
                l += 1
            else:
                sa = arr[r] * (2 * s + arr[r] - 1) // 2
                res += sa * id
                arr[l] -= arr[r]
                s += arr[r]
                r -= 2
                id -= 1

    return res


def part2(data):
    m = len(data)
    files = defaultdict(int)
    gaps = []
    s = 0
    for i in range(m):
        if i % 2 == 0:
            files[i // 2] = (s, int(data[i]))
        else:
            gaps.append([s, int(data[i])])
        s += int(data[i])

    gaps.sort(key=lambda x: x[0])
    for v in sorted(files.keys(), reverse=True):
        s, l = files[v]
        for gap in gaps:
            if gap[0] < s and gap[1] >= l:
                files[v] = (gap[0], l)
                new_start = gap[0] + l
                new_len = gap[1] - l
                gap[0], gap[1] = new_start, new_len
                break

    res = 0
    for k, v in files.items():
        res += k * v[1] * (2 * v[0] + v[1] - 1) // 2

    return res


if __name__ == "__main__":
    path = "day9/9.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
