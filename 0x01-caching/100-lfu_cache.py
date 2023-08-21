#!/usr/bin/env python3
"""LFU caching"""
from base_caching import BaseCaching
from collections import defaultdict
import heapq


class LFUCache(BaseCaching):
    """LFU caching"""

    def __init__(self):
        """Initialize LFU cache."""
        super().__init__()
        # To track usage frequencies of keys
        self.LFU_tracker = defaultdict(int)

    def put(self, key, item):
        """Add a new item to the cache while adhering to LFU behavior."""
        if key is None or item is None:
            return

        # Check if key is not already in the cache and cache is full
        if (key not in self.cache_data
                and len(self.cache_data)) >= self.MAX_ITEMS:
            # Find and discard the least frequently used key
            key_to_discard = heapq.nsmallest(1,
                                             self.LFU_tracker.items(),
                                             key=lambda item: item[1])[0][0]
            print(f'DISCARD: {key_to_discard}')
            self.LFU_tracker.pop(key_to_discard)
            self.cache_data.pop(key_to_discard)

        # Add the new item to the cache and update its frequency count
        self.cache_data[key] = item
        self.LFU_tracker[key] += 1

    def get(self, key):
        """Retrieve an item from the cache while
            updating its frequency count."""
        if key in self.cache_data:
            # Increment frequency count for accessed key
            self.LFU_tracker[key] += 1
        # Return the item associated with the key
        return self.cache_data.get(key)
