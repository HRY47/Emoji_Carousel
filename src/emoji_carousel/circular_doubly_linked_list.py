from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class _Node:
    data: str
    next: "_Node"
    prev: "_Node"

    def __init__(self, data: str) -> None:
        # Point to self to keep the list circular even for one node.
        self.data = data
        self.next = self
        self.prev = self


class CircularDoublyLinkedList:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self._capacity = capacity
        self._size = 0
        self._current: Optional[_Node] = None

    def add(self, item: str) -> None:
        # Add the first item to an empty list.
        if self._size != 0:
            raise ValueError("List already initialized; use insert().")
        self._ensure_space()
        self._current = _Node(item)
        self._size = 1

    def insert(self, position: str, item: str) -> None:
        # Insert left or right of the current node.
        if self._size == 0:
            self.add(item)
            return
        self._ensure_space()
        if position not in {"left", "right"}:
            raise ValueError("Position must be 'left' or 'right'.")

        current = self._require_current()
        node = _Node(item)
        if position == "left":
            left = current.prev
            node.prev = left
            node.next = current
            left.next = node
            current.prev = node
        else:
            right = current.next
            node.next = right
            node.prev = current
            right.prev = node
            current.next = node
        self._current = node
        self._size += 1

    def move_left(self) -> str:
        current = self._require_current()
        self._current = current.prev
        return self._current.data

    def move_right(self) -> str:
        current = self._require_current()
        self._current = current.next
        return self._current.data

    def peek_left(self) -> str:
        current = self._require_current()
        return current.prev.data

    def peek_right(self) -> str:
        current = self._require_current()
        return current.next.data

    def current_item(self) -> str:
        current = self._require_current()
        return current.data

    def remove(self) -> str:
        # Remove the current node and move focus to the left neighbor.
        current = self._require_current()
        removed = current.data
        if self._size == 1:
            self._current = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self._current = current.prev
        self._size -= 1
        return removed

    def size(self) -> int:
        return self._size

    def to_list(self) -> List[str]:
        # Snapshot items starting from the current node.
        if self._size == 0:
            return []
        items: List[str] = []
        current = self._require_current()
        items.append(current.data)
        node = current.next
        while node is not current:
            items.append(node.data)
            node = node.next
        return items

    def replace_items(self, items: List[str]) -> None:
        # Replace all items while keeping the carousel circular.
        if len(items) > self._capacity:
            raise ValueError("Carousel is full.")
        if not items:
            self._current = None
            self._size = 0
            return

        nodes = [_Node(item) for item in items]
        count = len(nodes)
        for index, node in enumerate(nodes):
            node.prev = nodes[index - 1]
            node.next = nodes[(index + 1) % count]
        self._current = nodes[0]
        self._size = count

    def _ensure_space(self) -> None:
        # Enforce the fixed capacity.
        if self._size >= self._capacity:
            raise ValueError("Carousel is full.")

    def _require_current(self) -> _Node:
        if self._current is None:
            raise IndexError("Carousel is empty.")
        return self._current
