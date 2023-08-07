#!/usr/bin/env python3
'''imports wait_random method'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns an array of floats'''
    res = [await wait_random(max_delay) for i in range(0, n)]
    return sorted(res)
