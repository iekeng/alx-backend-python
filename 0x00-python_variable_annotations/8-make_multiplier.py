#!/usr/bin python3
'''makes multiplier effect'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a callable object'''
    return lambda x: multiplier * multiplier