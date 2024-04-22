#!/usr/bin/env python3
"""returns a list sum as a float"""


def sum_list(input_list: list[float]) -> float:
    """
    Sums the elements of a list
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
