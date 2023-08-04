#!/usr/bin/env python3
"""ALX SE"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of floats in a list"""
    return sum(x for x in input_list)
