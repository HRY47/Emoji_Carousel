import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emoji_carousel.circular_doubly_linked_list import CircularDoublyLinkedList


def main() -> None:
    carousel = CircularDoublyLinkedList(5)
    carousel.add("@")
    carousel.insert("left", "#")
    carousel.insert("right", "$")
    print("Items:", carousel.to_list())
    print("Current:", carousel.current_item())
    print("Left:", carousel.peek_left())
    print("Right:", carousel.peek_right())


if __name__ == "__main__":
    main()
