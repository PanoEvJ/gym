from typing import TypeVar

T = TypeVar("T")


def process_numbers(numbers: list[int]) -> list[int]:
    return [number + 1 for number in numbers]


def process_elements(elements: list[T]) -> list[T]:
    return [element for index, element in enumerate(elements) if index % 2 == 1]


def main():
    print(process_numbers([1, 2, 3]))


if __name__ == "__main__":
    main()
