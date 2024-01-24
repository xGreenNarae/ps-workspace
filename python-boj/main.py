def resolver(input_lines: list[str]):
    # main logic
    sum_list = []
    for line in input_lines:
        sum_list.append(sum(map(int, line.split())))

    return list(map(str, sum_list))


def main():
    with open("input.txt", 'r') as file:
        input_lines = file.read().strip().split('\n')

    output_lines = resolver(input_lines)

    for line in output_lines:
        print(line)


if __name__ == "__main__":
    main()
