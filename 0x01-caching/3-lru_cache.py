#!/usr/bin/env python3
"""LRU caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU caching"""

    def __init__(self):
        super().__init__()
        self.LRU_tracker = OrderedDict()

    def put(self, key, item):
        """adds new item to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.LRU_tracker.move_to_end(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            least_used_key, _ = self.LRU_tracker.popitem(last=False)
            print(f'DISCARD: {least_used_key}')
            self.cache_data.pop(least_used_key)
        self.cache_data[key] = item
        self.LRU_tracker[key] = 0

    def get(self, key):
        """retrieves item from cache"""
        if key in self.cache_data:
            self.LRU_tracker.move_to_end(key)
        return self.cache_data.get(key)
