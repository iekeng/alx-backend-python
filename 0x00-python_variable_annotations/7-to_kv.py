#!/usr/bin/env python3
'''processes a mixed tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns the square of v and the string k'''
    return (k, v**2)
