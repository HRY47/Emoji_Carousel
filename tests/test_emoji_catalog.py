import unittest

from emoji_carousel.emoji_catalog import (
    find_by_name,
    find_by_symbol,
    list_by_category,
    load_catalog,
    search_catalog,
)


class TestEmojiCatalog(unittest.TestCase):
    def test_find_by_name(self) -> None:
        catalog = load_catalog()
        info = find_by_name(catalog, "grape")
        self.assertIsNotNone(info)
        self.assertEqual(info.name, "grape")
        self.assertEqual(info.symbol, "🍇")
        self.assertEqual(info.category, "food")

    def test_find_by_symbol(self) -> None:
        catalog = load_catalog()
        info = find_by_symbol(catalog, "🐶")
        self.assertIsNotNone(info)
        self.assertEqual(info.symbol, "🐶")
        self.assertEqual(info.category, "animals")

    def test_search_by_partial_name(self) -> None:
        catalog = load_catalog()
        results = search_catalog(catalog, "apple")
        names = {item.name for item in results}
        self.assertIn("red apple", names)
        self.assertIn("green apple", names)

    def test_search_by_category(self) -> None:
        catalog = load_catalog()
        results = search_catalog(catalog, "food")
        self.assertTrue(any(item.category == "food" for item in results))

    def test_list_by_category(self) -> None:
        catalog = load_catalog()
        results = list_by_category(catalog, "animals")
        self.assertTrue(any(item.category == "animals" for item in results))


if __name__ == "__main__":
    unittest.main()
