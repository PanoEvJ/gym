from typing import TypeVar, TypeAlias

T = TypeVar("T")

# A non-generic type alias
IntOrStr = int | str

# A generic type alias
ListOrSet: TypeAlias = list[T] | set[T]

def main():


if __name__ == "__main__":
    main()
