import sys


def resolver(input_lines: list[str]):
    input_cursor = iter(input_lines)
    output_lines: list[str] = []

    # main logic
    n = int(next(input_cursor))
    boards = list(map(int, next(input_cursor).split()))
    result: list = [0] * n

    for i in range(n - 1, -1, -1):
        refer_index = boards[i] + 1 + i
        if refer_index >= n:
            result[i] = 1
        else:
            result[i] = 1 + result[refer_index]

    output_lines.append(' '.join(map(str, result)))
    return output_lines


def main():
    input_lines = sys.stdin.read().splitlines()

    output_lines = resolver(input_lines)

    for line in output_lines:
        print(line)


if __name__ == "__main__":
    main()
