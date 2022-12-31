def fibonacci_with_memo(n: int, memo: dict = {}) -> int:
    if n == 0 or n == 1:
        return n

    if not memo.get(n):
        memo[n] = fibonacci_with_memo(n - 2, memo) + fibonacci_with_memo(n - 1, memo)

    return memo[n]


def fibonacci_bottom_up(n: int) -> int:
    if n == 0:
        return 0

    a: int = 0
    b: int = 1
    for _ in range(1, n):
        temp: int = a
        a = b
        b = temp + a

    return b


def add_until_100(numbers: list[int]) -> int:
    if not numbers:
        return 0

    sum_of_remaining_numbers: int = add_until_100(numbers[1:])
    if numbers[0] + sum_of_remaining_numbers > 100:
        return sum_of_remaining_numbers
    else:
        return numbers[0] + sum_of_remaining_numbers


def golamb(n: int, memo: dict = {}) -> int:
    if n == 1:
        return 1

    if not memo.get(n):
        memo[n] = 1 + golamb(n - golamb(golamb(n - 1, memo), memo), memo)

    return memo[n]


def count_unique_paths(
    num_rows: int,
    num_cols: int,
    memo: dict = {},
) -> int:
    """Returns the number of unique paths from the top-left square of a grid
    to the bottom right square, given a grid of N rows and columns
    and moving either one step right or one step down"""
    if num_rows == 1 or num_cols == 1:
        return 1

    if not memo.get((num_rows, num_cols)):
        memo[(num_rows, num_cols)] = count_unique_paths(
            num_rows - 1, num_cols, memo
        ) + count_unique_paths(num_rows, num_cols - 1, memo)

    return memo[(num_rows, num_cols)]
