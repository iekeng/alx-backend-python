#!/usr/bin/env python3
'''ducktype for a sequence'''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a list of lists'''
    return [(i, len(i)) for i in lst]
