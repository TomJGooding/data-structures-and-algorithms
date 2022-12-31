from data_structures_and_algorithms.recursion import (
    calculate_number_of_paths,
    count_characters,
    count_unique_paths,
    countdown,
    factorial,
    find_all_anagrams_of,
    find_evens_in,
    print_all_items,
)


def test_countdown(capfd):
    number = 10
    countdown(number)
    out, _ = capfd.readouterr()
    assert out == "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n0\n"


def test_factorial():
    number = 5
    actual = factorial(number)
    expected = 120
    assert actual == expected


def test_print_all_items(capfd):
    multidimensional_list = [
        1,
        2,
        3,
        [4, 5, 6],
        7,
        [
            8,
            [
                9,
                10,
            ],
        ],
    ]
    print_all_items(multidimensional_list)
    out, _ = capfd.readouterr()
    assert out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"


def test_calculate_number_of_paths():
    assert calculate_number_of_paths(number_steps=1) == 1
    assert calculate_number_of_paths(number_steps=2) == 2
    assert calculate_number_of_paths(number_steps=3) == 4
    assert calculate_number_of_paths(number_steps=4) == 7


def test_find_all_anagrams_of():
    assert find_all_anagrams_of("a") == ["a"]
    assert find_all_anagrams_of("ab") == ["ab", "ba"]
    assert find_all_anagrams_of("abc") == [
        "abc",
        "bac",
        "bca",
        "acb",
        "cab",
        "cba",
    ]
    assert len(find_all_anagrams_of("abcde")) == 120  # factorial!


def test_count_characters():
    assert count_characters([]) == 0
    assert count_characters(["ab"]) == 2
    assert count_characters(["ab", "c"]) == 3
    assert count_characters(["ab", "c", "def", "ghij"]) == 10


def test_find_evens_in():
    assert find_evens_in([]) == []
    assert find_evens_in([1]) == []
    assert find_evens_in([2]) == [2]
    assert find_evens_in([1, 2, 3]) == [2]
    assert find_evens_in([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 4, 6, 8, 10]


def test_count_unique_paths():
    assert count_unique_paths(num_rows=1, num_cols=3) == 1
    assert count_unique_paths(num_rows=3, num_cols=1) == 1
    assert count_unique_paths(num_rows=3, num_cols=3) == 6
    assert count_unique_paths(num_rows=3, num_cols=7) == 28
