#!/usr/bin/env python3
'''float module'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''sums a mixed list of floats and integers'''
    return sum(mxd_lst)
