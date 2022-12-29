from data_structures_and_algorithms.recursion import (
    countdown,
    factorial,
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
