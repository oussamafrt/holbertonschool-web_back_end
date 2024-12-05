#!/usr/bin/env python3
"""Shebang script"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function that takes  strings, integers and floats as arguments"""
    return (k, float(v ** 2))
