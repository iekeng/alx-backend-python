#!/usr/bin/env python3
'''imports task_wait_random method'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns an array of floats'''
    res = [await task_wait_random(max_delay) for i in range(0, n)]
    return sorted(res)
