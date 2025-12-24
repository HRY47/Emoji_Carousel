import difflib
import os
import random
import time
from typing import Dict, List, Optional

from . import art
from .circular_doubly_linked_list import CircularDoublyLinkedList
from .emoji_catalog import (
    EmojiInfo,
    find_by_name,
    find_by_symbol,
    iter_emojis,
    list_by_category,
    list_categories,
    load_catalog,
    search_catalog,
)

MAX_SIZE = 5
FRAME_DELAY = 0.2

try:
    from colorama import Fore, Style, init as colorama_init

    colorama_init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:  # pragma: no cover - optional dependency
    COLORAMA_AVAILABLE = False
    Fore = Style = None

COLOR_MAP: Dict[str, str] = {
    "food": Fore.GREEN if COLORAMA_AVAILABLE else "",
    "animals": Fore.YELLOW if COLORAMA_AVAILABLE else "",
}


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def render_current_frame(carousel: CircularDoublyLinkedList) -> None:
    # Render the current carousel state as a transition frame.
    size = carousel.size()
    if size == 0:
        return
    clear_screen()
    if size == 1:
        art.one_item_print(carousel.current_item())
    else:
        art.three_item_print(
            carousel.peek_left(),
            carousel.current_item(),
            carousel.peek_right(),
        )
    time.sleep(FRAME_DELAY)


def action_sequence(carousel: CircularDoublyLinkedList, action: str) -> None:
    # Render the transition art for a move/delete action.
    render_current_frame(carousel)
    clear_screen()
    size = carousel.size()
    if action == "del" and size == 1:
        art.last_del()
    elif action == "del" and size >= 2:
        art.not_last_del(carousel.peek_left(), carousel.peek_right())
    elif action == "l" and size >= 2:
        art.print_going_left(carousel.peek_left(), carousel.peek_right())
    elif action == "r" and size >= 2:
        art.print_going_right(carousel.peek_left(), carousel.peek_right())
    time.sleep(FRAME_DELAY * 3)


def add_sequence(carousel: CircularDoublyLinkedList, position: str) -> None:
    # Render the transition art for an add action.
    render_current_frame(carousel)
    clear_screen()
    size = carousel.size()
    if size == 0:
        art.first_add()
    elif position == "left" and size == 1:
        art.print_adding_left_one()
    elif position == "left" and size >= 2:
        art.print_adding_left_two(carousel.peek_left(), carousel.peek_right())
    elif position == "right" and size == 1:
        art.print_adding_right_one()
    elif position == "right" and size >= 2:
        art.print_adding_right_two(carousel.peek_left(), carousel.peek_right())
    time.sleep(FRAME_DELAY * 3)


def sample_names(catalog: List[dict], limit: int = 8) -> List[str]:
    # Grab a small set of example names for the prompt.
    names: List[str] = []
    for group in catalog:
        for name in group.get("emojis", {}).keys():
            names.append(name)
            if len(names) >= limit:
                return names
    return names


def render_prompt(
    carousel: CircularDoublyLinkedList,
    scenario: int,
    catalog: List[dict],
    position_index: int,
) -> None:
    # Scenario-based prompts keep the UI consistent.
    size = carousel.size()
    if size == 0 and scenario == 0:
        clear_screen()
        print("Type any of the following commands to perform the action:")
        print("  ADD: Add an emoji frame")
        print("  CATEGORY: Browse a category")
        print("  RANDOM: Add a random emoji")
        print("  SHUFFLE: Randomize carousel order")
        print("  SEARCH: Find emojis by name or category")
        print("  UNDO: Undo the last action")
        print("  Q: Quit the program")
    elif size == 0 and scenario == 1:
        print("What do you want to add?")
        examples = sample_names(catalog)
        if examples:
            print(f"Examples: {', '.join(examples)}")
    elif size == 1 and scenario == 0:
        clear_screen()
        art.one_item_print(carousel.current_item())
        print(f"Position: {position_index}/{size}")
        print("Type any of the following commands to perform the action:")
        print("  ADD: Add an emoji frame")
        print("  CATEGORY: Browse a category")
        print("  RANDOM: Add a random emoji")
        print("  SHUFFLE: Randomize carousel order")
        print("  SEARCH: Find emojis by name or category")
        print("  DEL: Delete current emoji frame")
        print("  INFO: Retrieve info about current frame")
        print("  UNDO: Undo the last action")
        print("  Q: Quit the program")
    elif size > 1 and size != MAX_SIZE and scenario == 0:
        clear_screen()
        art.three_item_print(
            carousel.peek_left(),
            carousel.current_item(),
            carousel.peek_right(),
        )
        print(f"Position: {position_index}/{size}")
        print("Type any of the following commands to perform the action:")
        print("  L: Move left")
        print("  R: Move right")
        print("  ADD: Add an emoji frame")
        print("  CATEGORY: Browse a category")
        print("  RANDOM: Add a random emoji")
        print("  SHUFFLE: Randomize carousel order")
        print("  SEARCH: Find emojis by name or category")
        print("  DEL: Delete current emoji frame")
        print("  INFO: Retrieve info about current frame")
        print("  UNDO: Undo the last action")
        print("  Q: Quit the program")
    elif size == MAX_SIZE and scenario == 0:
        clear_screen()
        art.three_item_print(
            carousel.peek_left(),
            carousel.current_item(),
            carousel.peek_right(),
        )
        print(f"Position: {position_index}/{size}")
        print("Type any of the following commands to perform the action:")
        print("  L: Move left")
        print("  R: Move right")
        print("  SHUFFLE: Randomize carousel order")
        print("  SEARCH: Find emojis by name or category")
        print("  DEL: Delete current emoji frame")
        print("  INFO: Retrieve info about current frame")
        print("  UNDO: Undo the last action")
        print("  Q: Quit the program")
    elif size != 0 and scenario == 1:
        print("What do you want to add?")
    elif size != 0 and scenario == 2:
        print("On which side do you want to add emoji frame? (left/right):")
    elif scenario == 3:
        print("Search by emoji name or category:")
    elif scenario == 4:
        categories = list_categories(catalog)
        print("Pick a category:")
        if categories:
            print(", ".join(categories))


def get_input(
    carousel: CircularDoublyLinkedList,
    catalog: List[dict],
    position_index: int,
) -> List[str]:
    # Collect user input and normalize to lower-case commands.
    size = carousel.size()
    inputs: List[str] = []
    render_prompt(carousel, 0, catalog, position_index)
    command = input(">> ").strip().lower()
    if command == "add" and size == 0:
        inputs.append(command)
        render_prompt(carousel, 1, catalog, position_index)
        inputs.append(input(">> ").strip().lower())
    elif command == "add" and size > 0 and size != MAX_SIZE:
        inputs.append(command)
        render_prompt(carousel, 1, catalog, position_index)
        inputs.append(input(">> ").strip().lower())
        render_prompt(carousel, 2, catalog, position_index)
        inputs.append(input(">> ").strip().lower())
    elif command == "search":
        inputs.append(command)
        render_prompt(carousel, 3, catalog, position_index)
        inputs.append(input(">> ").strip().lower())
    elif command == "category":
        inputs.append(command)
        render_prompt(carousel, 4, catalog, position_index)
        inputs.append(input(">> ").strip().lower())
    elif command == "random":
        inputs.append(command)
        if size > 0 and size != MAX_SIZE:
            render_prompt(carousel, 2, catalog, position_index)
            inputs.append(input(">> ").strip().lower())
    else:
        inputs.append(command)
    return inputs


def info_prompt(item: EmojiInfo) -> None:
    # Present details about the current emoji.
    print(f"Object: {colorize(item.name, item.category)}")
    print(f"Sym: {colorize(item.symbol, item.category)}")
    print(f"Class: {colorize(item.category, item.category)}\n")
    input("Press enter to continue ")


def add_item(carousel: CircularDoublyLinkedList, symbol: str, direction: str) -> None:
    # Insert the first item or expand left/right depending on the state.
    if carousel.size() == 0:
        carousel.add(symbol)
    else:
        carousel.insert(direction, symbol)


def colorize(text: str, category: str) -> str:
    if not COLORAMA_AVAILABLE:
        return text
    color = COLOR_MAP.get(category.lower(), Fore.CYAN)
    return f"{color}{text}{Style.RESET_ALL}"


def shuffle_carousel(carousel: CircularDoublyLinkedList) -> None:
    # Shuffle the carousel in-place while keeping size constant.
    items = carousel.to_list()
    random.shuffle(items)
    carousel.replace_items(items)


def render_matches(matches: List[EmojiInfo]) -> None:
    # Show matches in a compact list for selection.
    if not matches:
        print("No matches found.")
        return
    print("Matches:")
    for item in matches:
        label = f"{item.name} {item.symbol} ({item.category})"
        print(f"  {colorize(label, item.category)}")


def fuzzy_suggestions(catalog: List[dict], query: str) -> List[str]:
    names = [item.name for item in iter_emojis(catalog)]
    return difflib.get_close_matches(query, names, n=5, cutoff=0.6)


def resolve_add_name(catalog: List[dict], query: str) -> Optional[EmojiInfo]:
    # Resolve a name by exact match or prompt from search results.
    exact = find_by_name(catalog, query)
    if exact:
        return exact
    suggestions = fuzzy_suggestions(catalog, query)
    if suggestions:
        print("Did you mean:")
        for name in suggestions:
            print(f"  {name}")
    matches = search_catalog(catalog, query)
    render_matches(matches)
    selection = input("Pick a name from the list (blank to cancel): ").strip().lower()
    if not selection:
        return None
    return find_by_name(catalog, selection)


def wrap_index(index: int, size: int) -> int:
    if size == 0:
        return 0
    if index < 1:
        return size
    if index > size:
        return 1
    return index


def index_after_insert(index: int, size_before: int, direction: str) -> int:
    if size_before == 0:
        return 1
    delta = -1 if direction == "left" else 1
    return wrap_index(index + delta, size_before + 1)


def index_after_move(index: int, size: int, direction: str) -> int:
    delta = -1 if direction == "left" else 1
    return wrap_index(index + delta, size)


def index_after_remove(index: int, size_before: int) -> int:
    size_after = size_before - 1
    if size_after == 0:
        return 0
    return wrap_index(index - 1, size_after)


def main() -> None:
    # Main input loop for the CLI carousel.
    clear_screen()
    carousel = CircularDoublyLinkedList(MAX_SIZE)
    catalog = load_catalog()
    all_emojis = list(iter_emojis(catalog))
    history: List[Dict[str, str]] = []
    position_index = 0
    running = True
    while running:
        user_input = get_input(carousel, catalog, position_index)
        command = user_input[0]
        if command == "q":
            running = False
        elif command == "add" and carousel.size() < MAX_SIZE:
            size_before = carousel.size()
            emoji = resolve_add_name(catalog, user_input[1])
            if not emoji:
                print("No emoji selected.")
                time.sleep(1)
                continue
            if len(user_input) == 3:
                add_sequence(carousel, user_input[2])
                add_item(carousel, emoji.symbol, user_input[2])
                position_index = index_after_insert(position_index, size_before, user_input[2])
            else:
                add_sequence(carousel, "")
                add_item(carousel, emoji.symbol, "")
                position_index = index_after_insert(position_index, size_before, "right")
            history.append({"type": "add"})
        elif command == "info" and carousel.size() >= 1:
            emoji_info = find_by_symbol(catalog, carousel.current_item())
            if emoji_info:
                info_prompt(emoji_info)
        elif command == "del" and carousel.size() >= 1:
            size_before = carousel.size()
            action_sequence(carousel, command)
            removed = carousel.remove()
            position_index = index_after_remove(position_index, size_before)
            history.append({"type": "delete", "symbol": removed, "size_before": str(size_before)})
        elif command == "l" and carousel.size() > 1:
            action_sequence(carousel, command)
            carousel.move_left()
            position_index = index_after_move(position_index, carousel.size(), "left")
            history.append({"type": "move", "direction": "left"})
            render_current_frame(carousel)
        elif command == "r" and carousel.size() > 1:
            action_sequence(carousel, command)
            carousel.move_right()
            position_index = index_after_move(position_index, carousel.size(), "right")
            history.append({"type": "move", "direction": "right"})
            render_current_frame(carousel)
        elif command == "search":
            matches = search_catalog(catalog, user_input[1])
            render_matches(matches)
            input("Press enter to continue ")
        elif command == "category":
            category = user_input[1]
            matches = list_by_category(catalog, category)
            render_matches(matches)
            if not matches:
                input("Press enter to continue ")
                continue
            if carousel.size() >= MAX_SIZE:
                input("Press enter to continue ")
                continue
            selection = input("Pick a name to add (blank to cancel): ").strip().lower()
            if not selection:
                continue
            size_before = carousel.size()
            emoji = find_by_name(catalog, selection)
            if not emoji:
                print("Invalid emoji name.")
                time.sleep(1)
                continue
            direction = ""
            if size_before > 0:
                direction = input("Add left or right? (left/right): ").strip().lower()
                if direction not in {"left", "right"}:
                    print("Invalid direction.")
                    time.sleep(1)
                    continue
            add_sequence(carousel, direction)
            add_item(carousel, emoji.symbol, direction)
            position_index = index_after_insert(position_index, size_before, direction or "right")
            history.append({"type": "add"})
        elif command == "shuffle":
            if carousel.size() <= 1:
                print("Not enough items to shuffle.")
                time.sleep(1)
                continue
            shuffle_carousel(carousel)
            position_index = 1
        elif command == "random" and carousel.size() < MAX_SIZE:
            size_before = carousel.size()
            if not all_emojis:
                print("No emojis available.")
                time.sleep(1)
                continue
            emoji = random.choice(all_emojis)
            if carousel.size() == 0:
                add_sequence(carousel, "")
                add_item(carousel, emoji.symbol, "")
                position_index = index_after_insert(position_index, size_before, "right")
            else:
                direction = user_input[1] if len(user_input) > 1 else "right"
                if direction not in {"left", "right"}:
                    print("Invalid direction.")
                    time.sleep(1)
                    continue
                add_sequence(carousel, direction)
                add_item(carousel, emoji.symbol, direction)
                position_index = index_after_insert(position_index, size_before, direction)
            history.append({"type": "add"})
        elif command == "undo":
            if not history:
                print("Nothing to undo.")
                time.sleep(1)
                continue
            action = history.pop()
            if action["type"] == "add":
                size_before = carousel.size()
                if size_before == 0:
                    continue
                carousel.remove()
                position_index = index_after_remove(position_index, size_before)
            elif action["type"] == "delete":
                size_before = int(action["size_before"])
                symbol = action["symbol"]
                if size_before == 1:
                    carousel.add(symbol)
                    position_index = 1
                else:
                    carousel.insert("right", symbol)
                    position_index = index_after_insert(position_index, size_before - 1, "right")
            elif action["type"] == "move":
                direction = action["direction"]
                opposite = "right" if direction == "left" else "left"
                if opposite == "left":
                    carousel.move_left()
                else:
                    carousel.move_right()
                position_index = index_after_move(position_index, carousel.size(), opposite)
        else:
            print("Invalid command.")
            time.sleep(1)


if __name__ == "__main__":
    main()
