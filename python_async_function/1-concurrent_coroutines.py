#!/usr/bin/env python3
""" Module that takes an integer n and an integer max_delay as arguments"""

import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay and return
    the list of delays in ascending order"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
