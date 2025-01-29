from typing import Protocol, Self, Any, TypeVar
import sys

class SupportsMul(Protocol):
    def __mul__(self, other: Any) -> Self: ...

M = TypeVar('M', bound=SupportsMul)

def double(value: M):
    return value.__mul__(2)

if __name__ == "__main__":
    print(double(object()))
    print(sys.stderr)
