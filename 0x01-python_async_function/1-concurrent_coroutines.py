#!/usr/bin/env python3
'''imports wait_random method'''
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> [float]:
    '''Returns an array of floats'''
    delays = [await wait_random(max_delay) for i in range(0, n)]
    return delays