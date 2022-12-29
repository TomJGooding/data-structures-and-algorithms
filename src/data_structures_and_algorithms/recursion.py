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
