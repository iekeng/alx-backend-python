#!/usr/bin/env python3
'''Python async comprehension being used'''
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''returns a list of values yielded by async_generator'''
    return [x async for x in async_generator()]
