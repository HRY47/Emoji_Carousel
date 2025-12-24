import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from emoji_carousel.circular_doubly_linked_list import CircularDoublyLinkedList


def main() -> None:
    carousel = CircularDoublyLinkedList(5)
    carousel.add("2")
    carousel.insert("left", "1")
    print("Initial:", carousel.to_list())
    carousel.insert("right", "3")
    print("After insert:", carousel.to_list())
    print("Move right:", carousel.move_right())
    print("Move left:", carousel.move_left())
    print("Removed:", carousel.remove())
    print("Remaining:", carousel.to_list())


if __name__ == "__main__":
    main()
