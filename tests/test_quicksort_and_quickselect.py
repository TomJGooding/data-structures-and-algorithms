from data_structures_and_algorithms.quicksort_and_quickselect import (
    SortableList,
    calc_greatest_product_of_three,
    find_max_with_big_o_n_log_n,
    find_max_with_big_o_of_n,
    find_max_with_big_o_squared,
    find_missing_number,
)


def test_calc_greatest_product_of_three():
    numbers = [0, 5, 2, 1, 6, 3]
    assert calc_greatest_product_of_three(numbers) == 90


def test_find_missing_number():
    numbers = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    assert find_missing_number(numbers) == 8


def test_find_max_with_big_o_squared():
    numbers = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    assert find_max_with_big_o_squared(numbers) == 9


def test_find_max_with_big_o_n_log_n():
    numbers = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    assert find_max_with_big_o_n_log_n(numbers) == 9


def test_find_max_with_big_o_of_n():
    numbers = [9, 3, 2, 5, 6, 7, 1, 0, 4]
    assert find_max_with_big_o_of_n(numbers) == 9


def test_sortable_list_quicksort():
    numbers = [0, 5, 2, 1, 6, 3]
    sortable_list = SortableList(numbers)
    sortable_list.quicksort()
    assert sortable_list.list_ == [0, 1, 2, 3, 5, 6]


def test_sortable_list_quickselect():
    numbers = [0, 5, 2, 1, 6, 3]
    sortable_list = SortableList(numbers)
    assert sortable_list.quickselect(kth_lowest_value=1) == 1
