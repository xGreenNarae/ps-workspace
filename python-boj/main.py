def resolver(input_lines: list[str]):
    input_cursor = iter(input_lines)

    # main logic
    input1 = next(input_cursor)
    input2 = next(input_cursor)

    return


def main():
    with open("input.txt", 'r') as file:
        input_lines = file.read().strip().split('\n')

    output_lines = resolver(input_lines)

    for line in output_lines:
        print(line)


if __name__ == "__main__":
    main()
