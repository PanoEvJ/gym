from typing import TypeVar

T = TypeVar("T")


def process_numbers(numbers: list[int]) -> list[int]:
    return [number + 1 for number in numbers]


def process_elements(elements: list[T]) -> list[T]:
    return [element for index, element in enumerate(elements) if index % 2 == 1]


def main():
    my_list = [1, 2, 3, 4, 5]
    processed = process_elements(elements=my_list)
    print(processed)

    my_str_list = ["a", "b", "c", "d", "e"]
    processed = process_elements(elements=my_str_list)
    print(processed)


if __name__ == "__main__":
    main()
