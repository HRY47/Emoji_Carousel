from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional


@dataclass(frozen=True)
class EmojiInfo:
    name: str
    symbol: str
    category: str


def load_catalog(path: Optional[Path] = None) -> List[dict]:
    # Load the catalog from disk (defaults to bundled data).
    if path is None:
        path = Path(__file__).resolve().parent / "data" / "emojis.json"
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def find_by_name(catalog: Iterable[dict], name: str) -> Optional[EmojiInfo]:
    # Look up an emoji by its human-readable name.
    for group in catalog:
        emojis = group.get("emojis", {})
        if name in emojis:
            return EmojiInfo(name=name, symbol=emojis[name], category=group.get("class", ""))
    return None


def find_by_symbol(catalog: Iterable[dict], symbol: str) -> Optional[EmojiInfo]:
    # Look up an emoji by its symbol.
    for group in catalog:
        emojis = group.get("emojis", {})
        for key, value in emojis.items():
            if value == symbol:
                return EmojiInfo(name=key, symbol=value, category=group.get("class", ""))
    return None


def iter_emojis(catalog: Iterable[dict]) -> Iterator[EmojiInfo]:
    # Yield every emoji in the catalog.
    for group in catalog:
        category = group.get("class", "")
        for name, symbol in group.get("emojis", {}).items():
            yield EmojiInfo(name=name, symbol=symbol, category=category)


def search_catalog(catalog: Iterable[dict], query: str) -> List[EmojiInfo]:
    # Match by category (exact) or partial name (case-insensitive).
    normalized = query.strip().lower()
    if not normalized:
        return []

    matches: Dict[str, EmojiInfo] = {}
    for group in catalog:
        category = group.get("class", "")
        category_match = category.lower() == normalized
        for name, symbol in group.get("emojis", {}).items():
            name_match = normalized in name.lower()
            if category_match or name_match:
                matches[name] = EmojiInfo(
                    name=name,
                    symbol=symbol,
                    category=category,
                )
    return list(matches.values())


def list_by_category(catalog: Iterable[dict], category: str) -> List[EmojiInfo]:
    # Return all emojis in a given category.
    normalized = category.strip().lower()
    if not normalized:
        return []
    matches: List[EmojiInfo] = []
    for group in catalog:
        if group.get("class", "").lower() != normalized:
            continue
        for name, symbol in group.get("emojis", {}).items():
            matches.append(EmojiInfo(name=name, symbol=symbol, category=group.get("class", "")))
    return matches


def list_categories(catalog: Iterable[dict]) -> List[str]:
    # List available categories in the catalog.
    categories = {group.get("class", "") for group in catalog}
    return sorted(category for category in categories if category)
