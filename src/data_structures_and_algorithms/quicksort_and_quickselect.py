import math
from typing import Optional


def calc_greatest_product_of_three(numbers: list[int]) -> int:
    return math.prod(sorted(numbers)[-3:])


def find_missing_number(numbers: list[int]) -> int | None:
    for idx, number in enumerate(sorted(numbers)):
        if number != idx:
            return idx

    return None


def find_max_with_big_o_squared(numbers: list[int]):
    for i in numbers:
        is_max: bool = True
        for j in numbers:
            if j > i:
                is_max = False
        if is_max:
            return i


def find_max_with_big_o_n_log_n(numbers: list[int]):
    return sorted(numbers)[-1]


def find_max_with_big_o_of_n(numbers: list[int]):
    max_so_far: int = numbers[0]
    for i in numbers:
        if i > max_so_far:
            max_so_far = i

    return max_so_far


class SortableList:
    def __init__(self, list_: list) -> None:
        self.list_: list = list_

    def quicksort(
        self,
        left_index: int = 0,
        right_index: Optional[int] = None,
    ) -> None:
        if right_index is None:
            right_index = len(self.list_) - 1

        if right_index - left_index <= 0:
            return

        pivot_index: int = self.partition(left_index, right_index)

        self.quicksort(left_index, pivot_index - 1)
        self.quicksort(pivot_index + 1, right_index)

    def quickselect(
        self,
        kth_lowest_value: int,
        left_index: int = 0,
        right_index: Optional[int] = None,
    ) -> object:
        if right_index is None:
            right_index = len(self.list_) - 1

        if right_index - left_index <= 0:
            return self.list_[left_index]

        pivot_index: int = self.partition(left_index, right_index)

        if kth_lowest_value < pivot_index:
            return self.quickselect(
                kth_lowest_value,
                left_index,
                pivot_index - 1,
            )
        elif kth_lowest_value > pivot_index:
            return self.quickselect(
                kth_lowest_value,
                pivot_index + 1,
                right_index,
            )
        else:
            return self.list_[pivot_index]

    def partition(self, left_pointer: int, right_pointer: int) -> int:
        pivot_index: int = right_pointer
        pivot: object = self.list_[pivot_index]
        right_pointer -= 1

        while True:
            while self.list_[left_pointer] < pivot:
                left_pointer += 1
            while self.list_[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self.list_[left_pointer], self.list_[right_pointer] = (
                    self.list_[right_pointer],
                    self.list_[left_pointer],
                )
                left_pointer += 1

        self.list_[left_pointer], self.list_[pivot_index] = (
            self.list_[pivot_index],
            self.list_[left_pointer],
        )

        return left_pointer
