#!/usr/bin/env python3
"""
FIFO caching module
"""

from collections import OrderedDict
from base_caching import FIFOCache


class FIFOCache(BaseCaching):
    """
    A class FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """
        initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item into the cache
        """
        if key is None and item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(false)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        Gets an item in the cache
        """
        return self.cache_data.get(key, None)
