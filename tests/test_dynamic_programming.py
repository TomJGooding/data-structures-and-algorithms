from data_structures_and_algorithms.dynamic_programming import (
    add_until_100,
    count_unique_paths,
    fibonacci_bottom_up,
    fibonacci_with_memo,
    golamb,
)


def test_fibonacci_with_memo():
    assert fibonacci_with_memo(0) == 0
    assert fibonacci_with_memo(1) == 1
    assert fibonacci_with_memo(5) == 5
    assert fibonacci_with_memo(10) == 55


def test_fibonacci_bottom_up():
    assert fibonacci_bottom_up(0) == 0
    assert fibonacci_bottom_up(1) == 1
    assert fibonacci_bottom_up(5) == 5
    assert fibonacci_bottom_up(10) == 55


def test_add_until_100():
    assert add_until_100([]) == 0
    assert add_until_100([1, 99]) == 100
    assert add_until_100([1, 2, 99]) == 100
    assert add_until_100([25, 26, 50]) == 76


def test_golamb():
    assert golamb(1) == 1
    assert golamb(2) == 2
    assert golamb(3) == 2
    assert golamb(4) == 3


def test_count_unique_paths():
    assert count_unique_paths(num_rows=1, num_cols=3) == 1
    assert count_unique_paths(num_rows=3, num_cols=1) == 1
    assert count_unique_paths(num_rows=3, num_cols=3) == 6
    assert count_unique_paths(num_rows=3, num_cols=7) == 28
