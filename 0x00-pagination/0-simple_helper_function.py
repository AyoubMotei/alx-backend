#!/usr/bin/env python3

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
