def process_numbers(numbers: list[int]) -> list[int]:
    return [number + 1 for number in numbers]


def main():
    print(process_numbers([1, 2, 3]))


if __name__ == "main":
    main()
