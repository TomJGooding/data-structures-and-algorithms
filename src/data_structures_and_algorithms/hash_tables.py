import string


def get_intersection(list1: list[int], list2: list[int]) -> list[int]:
    hash_table: dict = {}
    for i in list1:
        hash_table[i] = True

    intersection: list[int] = []
    for j in list2:
        if hash_table.get(j):
            intersection.append(j)

    return intersection


def find_duplicate(list: list[str]) -> str | None:
    hash_table: dict = {}
    for string_ in list:
        if hash_table.get(string_):
            return string_
        else:
            hash_table[string_] = True

    return None


def find_missing_letter(string_: str) -> str | None:
    hash_table: dict = {}
    for char in string_:
        hash_table[char] = True

    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if not hash_table.get(letter):
            return letter

    return None


def find_first_non_duplicate(string_) -> str | None:
    hash_table: dict = {}
    for char in string_:
        if hash_table.get(char):
            hash_table[char] += 1
        else:
            hash_table[char] = 1

    for char in string_:
        if hash_table[char] == 1:
            return char

    return None
