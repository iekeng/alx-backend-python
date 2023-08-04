#!/usr/bin/env python3
from typing import List
'''  returns a sum of floats '''


def sum_list(input_list: List[float]) -> float:
    ''' loops through the input_list and adds items in the sum variable '''
    sum = 0
    for i in range(0, len(input_list)):
        sum = sum + input_list[i]
    return sum
