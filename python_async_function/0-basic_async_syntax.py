#!/usr/bin/env python3
"""Shebang script"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
