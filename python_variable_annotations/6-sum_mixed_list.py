#!/usr/bin/env python3
"""
Calculate the sum of a list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list
    containing integers and floats.
    """

    return sum(mxd_lst)
