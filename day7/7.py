from utils import read_input, solve_part


def solve(res, vars, curr):
    if curr == res and not vars:
        return True
    if curr > res or not vars:
        return False
    return solve(res, vars[1:], curr + vars[0]) or solve(res, vars[1:], curr * vars[0])


def solve2(res, vars, curr):
    if curr == res and not vars:
        return True
    if curr > res or not vars:
        return False
    return (
        solve2(res, vars[1:], curr + vars[0])
        or solve2(res, vars[1:], curr * vars[0])
        or solve2(res, vars[1:], int(str(curr) + str(vars[0])))
    )


def eqs(data):
    return [
        (int(m), list(map(int, n.split())))
        for m, n in [line.split(":") for line in data.splitlines()]
    ]


def part1(data):
    return sum(res for res, vars in eqs(data) if solve(res, vars[1:], vars[0]))


def part2(data):

    return sum(
        res
        for res, vars in eqs(data)
        if solve(res, vars[1:], vars[0]) or solve2(res, vars[1:], vars[0])
    )


if __name__ == "__main__":
    path = "day7/7.txt"
    data = read_input(path)
    solve_part(part1, data)
    solve_part(part2, data)
