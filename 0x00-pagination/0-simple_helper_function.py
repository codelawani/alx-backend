#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """Generate list index range based on pagination params"""
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return (start_index, end_index)
