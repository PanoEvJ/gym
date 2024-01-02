from typing import TypeVar, TypeAlias, Generic

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

# generic function example
def get_first_item(items: list[T]) -> T:
    return items[0]

def main():


if __name__ == "__main__":
    main()
