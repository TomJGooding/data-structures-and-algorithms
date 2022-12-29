from data_structures_and_algorithms.hash_tables import (
    find_duplicate,
    find_first_non_duplicate,
    find_missing_letter,
    get_intersection,
)


def test_get_intersection():
    list1 = [1, 2, 3, 4, 5]
    list2 = [0, 2, 4, 6, 8]
    actual = get_intersection(list1, list2)
    expected = [2, 4]
    assert actual == expected


def test_find_duplicate():
    list = ["a", "b", "c", "d", "c", "e", "f"]
    actual = find_duplicate(list)
    expected = "c"
    assert actual == expected


def test_find_missing_letter():
    string_ = "the quick brown box jumps over the lazy dog"
    actual = find_missing_letter(string_)
    expected = "f"
    assert actual == expected


def test_find_first_non_duplicate():
    string_ = "minimum"
    actual = find_first_non_duplicate(string_)
    expected = "n"
    assert actual == expected
