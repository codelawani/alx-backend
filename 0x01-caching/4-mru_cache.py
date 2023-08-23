#!/usr/bin/env python3
"""MRU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU caching"""

    def __init__(self):
        super().__init__()
        self.MRU_tracker = OrderedDict()

    def put(self, key, item):
        """adds new item to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.MRU_tracker.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            most_used_key, _ = self.MRU_tracker.popitem()
            print(f'DISCARD: {most_used_key}')
            self.cache_data.pop(most_used_key)
        self.MRU_tracker[key] = 0
        self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        if key in self.cache_data:
            self.MRU_tracker.move_to_end(key)
        return self.cache_data.get(key)
