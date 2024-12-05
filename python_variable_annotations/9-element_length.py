#!/usr/bin/env python3
"""Shebang script"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function takes an iterable sequence as argument"""
    return [(i, len(i)) for i in lst]
