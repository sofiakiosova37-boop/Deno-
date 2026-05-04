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

def _finalize_log(result, start_time, level, func, args, timestamp):
    if level != "ERROR":  
        exec_time = time.perf_counter() - start_time
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "function": func.__name__,
            "args": str(args),
            "result": str(result),
            "execution_time": f"{exec_time:.4f}s"
        }
        log_func = getattr(logger, level.lower(), logger.info)
        log_func(json.dumps(log_entry))

def _handle_exception(e, start_time, func, args, timestamp):
    exec_time = time.perf_counter() - start_time
    log_entry = {
        "timestamp": timestamp,
        "level": "ERROR",
        "function": func.__name__,
        "args": str(args),
        "exception": str(e),
        "execution_time": f"{exec_time:.4f}s"
    }
    logger.error(json.dumps(log_entry))
    raise e

def log(level: str = "INFO"):
    def decorator(func):
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                timestamp = datetime.now().isoformat()
                try:
                    result = await func(*args, **kwargs) 
                    _finalize_log(result, start_time, level, func, args, timestamp)
                    return result
                except Exception as e:
                    _handle_exception(e, start_time, func, args, timestamp)
        else:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                timestamp = datetime.now().isoformat()
                try:
                    result = func(*args, **kwargs)
                    _finalize_log(result, start_time, level, func, args, timestamp)
                    return result
                except Exception as e:
                    _handle_exception(e, start_time, func, args, timestamp)
        return wrapper
    return decorator