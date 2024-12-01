import time


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def read_lines(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def read_ints(file_path):
    with open(file_path, "r") as file:
        return [int(line) for line in file.read().strip().split("\n")]


def read_csv(file_path):
    with open(file_path, "r") as file:
        return [line.split(",") for line in file.read().strip().split("\n")]


def lines_to_pairs(data):
    for line in data.splitlines():
        a, b = map(int, line.split())
        yield a, b


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time

        if duration >= 1:
            print(f"{func.__name__} execution time: {duration:.4f} seconds")
        elif duration >= 1e-3:
            print(f"{func.__name__} execution time: {duration * 1000:.4f} milliseconds")
        elif duration >= 1e-6:
            print(f"{func.__name__} execution time: {duration * 1e6:.4f} microseconds")
        else:
            print(f"{func.__name__} execution time: {duration * 1e9:.4f} nanoseconds")

    return wrapper


@execution_time
def solve_part(func, data):
    res = func(data)
    print(f"Result: {res}")
