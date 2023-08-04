#!/usr/bin/env python3
'''processes a sequence'''
from typing import Sequence, Union, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''accepts any kind of sequence and retuns any type of value'''
    if lst:
        return lst[0]
    else:
        return None
