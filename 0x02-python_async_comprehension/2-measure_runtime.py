#!/usr/bin/env python3
'''Imports async_comprehension'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures the execution time for executing
    four async_comprehension functions'''
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
