def countdown(number: int) -> None:
    print(number)
    if number == 0:
        return
    else:
        countdown(number - 1)


def factorial(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def print_all_items(multidimensional_list: list[int | list]) -> None:
    for item in multidimensional_list:
        if isinstance(item, list):
            print_all_items(item)
        else:
            print(item)


def calculate_number_of_paths(number_steps: int) -> int:
    """Returns the number of different possible paths that can be taken
    to reach the top of a staircase with N steps, where a person has the
    ability to climb one, two or three steps at a time"""
    if number_steps < 0:
        return 0
    elif number_steps in (1, 0):
        return 1
    else:
        return (
            calculate_number_of_paths(number_steps - 1)
            + calculate_number_of_paths(number_steps - 2)
            + calculate_number_of_paths(number_steps - 3)
        )


def find_all_anagrams_of(text: str) -> list[str]:
    if len(text) == 1:
        return [text[0]]

    substring_anagrams: list[str] = find_all_anagrams_of(text[1:])
    collection: list[str] = []
    for anagram in substring_anagrams:
        for i in range(0, len(anagram) + 1):
            anagram_letters = list(anagram)
            anagram_letters.insert(i, text[0])
            collection.append("".join(anagram_letters))

    return collection


def count_characters(strings: list[str]) -> int:
    if len(strings) == 0:
        return 0
    return len(strings[0]) + count_characters(strings[1:])


def find_evens_in(numbers: list[int]) -> list[int]:
    if not numbers:
        return []
    elif numbers[0] % 2 == 0:
        return [numbers[0]] + find_evens_in(numbers[1:])
    else:
        return find_evens_in(numbers[1:])


def count_unique_paths(num_rows: int, num_cols: int) -> int:
    """Returns the number of unique paths from the top-left square of a grid
    to the bottom right square, given a grid of N rows and columns
    and moving either one step right or one step down"""
    if num_rows == 1 or num_cols == 1:
        return 1
    return count_unique_paths(num_rows - 1, num_cols) + count_unique_paths(
        num_rows, num_cols - 1
    )
