from typing import Generic, TypeAlias, TypeVar

T = TypeVar("T")

# A non-generic type alias
IntOrStr = int | str

# A generic type alias
ListOrSet: TypeAlias = list[T] | set[T]


class Box(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item

    def get_item(self) -> T:
        return self.item

    def set_item(self, item: T) -> None:
        self.item = item


# generic function
def get_first_item(items: list[T]) -> T:
    return items[0]


def main():
    # for integers
    int_box = Box(item=123)
    print(int_box.get_item())

    # for strings
    str_box = Box(item="hello")
    print(str_box.get_item())

    # for lists
    list_box = Box(item=[1, 2, 3])
    print(list_box.get_item())

    # generic function example
    first_item = get_first_item(items=[1, 2, 3])
    print(first_item)


if __name__ == "__main__":
    main()
