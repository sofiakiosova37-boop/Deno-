import time
import functools
from functools import wraps
import json
import logging
import asyncio
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log(level="INFO"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return process_log(func, args, kwargs)
        return wrapper
    return decorator