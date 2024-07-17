#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def count_requests(fn: Callable) -> Callable:
    """ counting requests  """

    @wraps(fn)
    def wrapper(url):
        """ Wrapper for counting requests """
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        html = fn(url)
        redis.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """html"""
    r = requests.get(url)
    return r.text
