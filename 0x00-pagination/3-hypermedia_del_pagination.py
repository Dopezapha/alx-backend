#!/usr/bin/env python3
"""
Implement methods get_page, get_hyper, and get_hyper_index for
paginating a database of popular baby names.
"""
import csv
import math
from typing import List, Any, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        try:
            return get_page(page, page_size, data)
        except AssertionError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing pagination information.
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination information based on index.
        """
        assert index is None or (
                isinstance(index, int) and 0 <= index < len(self.dataset())
                ), "Invalid index"

        data = self.dataset()
        if index is None:
            index = 0

        next_index = index + page_size
        page_data = data[index:next_index]

        return {
            "index": index,
            "next_index": next_index if next_index < len(data) else None,
            "page_size": len(page_data),
            "data": page_data
        }


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


def get_page(page: int, page_size: int, data: List[Any]) -> List[Any]:
    """
    A method called get_page that takes two integers page and page_size
    and returns the appropriate page of the dataset
    """
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0
    if page > len(data) // page_size + (1 if len(data) % page_size else 0):
        return []
    start, end = index_range(page, page_size)
    return data[start:end]
