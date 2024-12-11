#!/usr/bin/env python3
"""shebang script"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indexes for a pagination system."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
