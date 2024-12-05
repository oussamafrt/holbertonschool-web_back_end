#!/usr/bin/env python3
"""Shebang script"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that takes a float as argument"""

    def multiplier_function(num: float) -> float:
        """ Function that takes a float as argument"""
        return num * multiplier

    return multiplier_function
