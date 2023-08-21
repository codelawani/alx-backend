#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system"""

    def put(self, key, item):
        """adds new item to cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        return self.cache_data.get(key)
