#!/usr/bin/env python3
'''Employs generic varible typing'''
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''Returns the value of a dicionary, given any value'''
    if key in dct:
        return dct[key]
    else:
        return default
