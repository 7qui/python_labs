from collections import deque
from typing import Any


class Stack:
    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty Stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


class Queue:
    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty Queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)!r})"


if __name__ == "__main__":
    # демо для скриншотов
    s = Stack()
    s.push(1)
    s.push(2)
    print("Stack:", s)
    print("pop:", s.pop())
    print("peek:", s.peek())

    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    print("Queue:", q)
    print("dequeue:", q.dequeue())
    print("peek:", q.peek())
