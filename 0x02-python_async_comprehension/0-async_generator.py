#!/usr/bin/env python3
'''async function generates yields random numbers'''
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    '''yields values between 0 and 10'''
    x: int = 10
    for i in range(x):
        await asyncio.sleep(1)
        yield random.uniform(0, x)
