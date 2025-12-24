import unittest

from emoji_carousel.circular_doubly_linked_list import CircularDoublyLinkedList


class TestCircularDoublyLinkedList(unittest.TestCase):
    def test_add_and_insert(self) -> None:
        carousel = CircularDoublyLinkedList(3)
        carousel.add("A")
        carousel.insert("left", "B")
        carousel.insert("right", "C")
        self.assertEqual(carousel.size(), 3)
        self.assertEqual(set(carousel.to_list()), {"A", "B", "C"})

    def test_move_and_peek(self) -> None:
        carousel = CircularDoublyLinkedList(3)
        carousel.add("A")
        carousel.insert("right", "B")
        carousel.insert("right", "C")
        left = carousel.peek_left()
        right = carousel.peek_right()
        self.assertNotEqual(left, right)
        current = carousel.current_item()
        carousel.move_left()
        self.assertNotEqual(current, carousel.current_item())

    def test_remove(self) -> None:
        carousel = CircularDoublyLinkedList(2)
        carousel.add("A")
        carousel.insert("right", "B")
        removed = carousel.remove()
        self.assertIn(removed, {"A", "B"})
        self.assertEqual(carousel.size(), 1)
        carousel.remove()
        self.assertEqual(carousel.size(), 0)

    def test_capacity_limit(self) -> None:
        carousel = CircularDoublyLinkedList(1)
        carousel.add("A")
        with self.assertRaises(ValueError):
            carousel.insert("left", "B")

    def test_invalid_position(self) -> None:
        carousel = CircularDoublyLinkedList(2)
        carousel.add("A")
        with self.assertRaises(ValueError):
            carousel.insert("up", "B")

    def test_replace_items(self) -> None:
        carousel = CircularDoublyLinkedList(3)
        carousel.replace_items(["A", "B", "C"])
        self.assertEqual(carousel.size(), 3)
        self.assertEqual(set(carousel.to_list()), {"A", "B", "C"})


if __name__ == "__main__":
    unittest.main()
