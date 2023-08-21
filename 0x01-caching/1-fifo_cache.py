#!/usr/bin/env python3
"""FIFO caching"""
from base_caching import BaseCaching
from collections import deque


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """adds new item to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            key_to_discard = self.queue.popleft()
            self.cache_data.pop(key_to_discard)
            print(f'DISCARD: {key_to_discard}')
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        return self.cache_data.get(key)
