#!/usr/bin/env python3
"""Transform a list of key-value pairs"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A list of tuples with the square of the value"""
    return (k, v**2)
