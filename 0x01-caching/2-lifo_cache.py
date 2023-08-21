#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching"""

    def put(self, key, item):
        """adds new item to cache"""
        if not key or not item:
            return
        if (len(self.cache_data) >= self.MAX_ITEMS
                and key not in self.cache_data):
            key_to_discard = list(self.cache_data.keys())[-1]
            print(f'DISCARD: {key_to_discard}')
            self.cache_data.pop(key_to_discard)
        self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        return self.cache_data.get(key)


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
