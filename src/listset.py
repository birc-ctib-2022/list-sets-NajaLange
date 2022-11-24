"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        self.data = list(init)

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        return x in self.data

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        if not self.data: 
            return False
        else: 
            return True
        

    def add(self, x: T) -> None:
        """Add x to the set."""
        self.data.append(x)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        self.data.remove(x)

#x = list(range(10))
#s = ListSet(x)
#print(s)

#print(s.__contains__(4))
#s.add(11)
#s.remove(11)
#print(s.__contains__(11))