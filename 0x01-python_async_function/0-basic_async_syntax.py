#!/usr/bin/env python3
'''wait_random async coroutine'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay between 0 and max_delay
       then returns max_delay
    '''
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
