#!/usr/bin/env python3
"""Shebang script"""


import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient pagination with hypermedia support."""
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset()), \
            "index must be a valid position within the dataset"

        data = []
        current_index = index
        indexed_data = self.indexed_dataset()
        keys = sorted(indexed_data.keys())

        for _ in range(page_size):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1
            if current_index >= len(keys):
                break

        next_index = current_index if current_index < len(keys) else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
