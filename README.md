# Emoji Carousel CLI

An interactive terminal carousel that lets you add, remove, and browse emoji
frames from a small catalog. The experience is powered by a circular doubly
linked list and a simple ASCII UI.

## Features
- Interactive carousel navigation (left/right)
- Add and delete emoji frames with capacity limits
- Lookup info about the current emoji
- Minimal dependencies (stdlib only)

## Project Layout
- `src/emoji_carousel/app.py` - CLI application
- `src/emoji_carousel/circular_doubly_linked_list.py` - core data structure
- `src/emoji_carousel/emoji_catalog.py` - emoji catalog loader and lookup
- `src/emoji_carousel/art.py` - ASCII UI artwork
- `src/emoji_carousel/data/emojis.json` - emoji catalog data
- `tests/` - unit tests
- `scripts/` - helper scripts (run app, run tests, demos)

## Run
From the project root:
```
python scripts/run_app.py
```

### Commands
- `add` - add a new emoji frame (prompts for name and direction)
- `category` - browse a category and choose an emoji to add
- `del` - delete current emoji frame
- `info` - show info about the current emoji
- `l` - move left
- `r` - move right
- `search` - list emojis by partial name or category
- `shuffle` - randomize carousel order
- `random` - add a random emoji frame
- `undo` - undo the last add/delete/move action
- `q` - quit

### Emoji Names
The emoji names come from `src/emoji_carousel/data/emojis.json`. Use the exact
names in that file (e.g., `grape`, `dog face`).

## Tests
Run all tests:
```
python scripts/run_tests.py
```

Alternative:
```
PYTHONPATH=src python -m unittest discover -s tests
```

## Notes
- Requires Python 3.8+.
- Optional: `colorama` adds colored category output (safe to omit).
  - Install with: `pip install colorama`
- The carousel capacity defaults to 5 frames in `src/emoji_carousel/app.py`.
- This project uses a `src/` layout; helper scripts set up `PYTHONPATH`.
