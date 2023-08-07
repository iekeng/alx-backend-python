#!/usr/bin/env python3
'''creates an async task'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''returns task'''
    task = asyncio.create_task(wait_random(max_delay))
    return task
