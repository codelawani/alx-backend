#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
from typing import Dict, List, Tuple, Union


def index_range(page: int, page_size: int) -> Tuple[int, ...]:
    """Generate list index range based on pagination params"""
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialise dataset"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get current page dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return [] if end >= len(data) else data[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[str, Union[int, List[List], None]]:
        """Hyper pagination"""
        data = self.get_page(page, page_size)
        _, end_index = index_range(page, page_size)
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        page_size = len(data)
        next_page = page + 1 if end_index < len(self.dataset()) else None
        prev_page = (page - 1) or None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
