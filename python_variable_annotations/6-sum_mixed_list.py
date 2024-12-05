#!/usr/bin/env python3
"""Shebang script"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[list, float]]) -> float:
    """function takes mixed types as arguments"""
    return (sum(mxd_lst))
