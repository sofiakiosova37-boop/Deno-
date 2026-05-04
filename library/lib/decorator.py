import time
import functools
from functools import wraps
import json
import logging
import asyncio
from datetime import datetime
import inspect

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def log(level="INFO"):
    def decorator(func):
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                return await _process_logging(func, args, kwargs, level, True)
        else:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return _process_logging(func, args, kwargs, level, False)
        return wrapper
    return decorator

def _process_logging(func, args, kwargs, level, is_async):
    start_time = time.perf_counter()
    timestamp = datetime.now().isoformat()