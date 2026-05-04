import time
import functools
from functools import wraps
import json
import logging
import asyncio
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log(level="INFO", structured=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            timestamp = datetime.now().isoformat()
            try:
                result = func(*args, **kwargs)
                exec_time = time.perf_counter() - start_time
                if level != "ERROR":
                    log_entry = {
                        "ts": timestamp,
                        "level": level,
                        "func": func.__name__,
                        "args": args,
                        "res": result,
                        "time": f"{exec_time:.5f}s"
                    }
                    msg = json.dumps(log_entry) if structured else f"[{timestamp}] {level}: {func.__name__}({args}) -> {result} в течение {exec_time:.5f}s"
                    logger.info(msg)
                return result
            except Exception as e:
                err_msg = f"[{timestamp}] ERROR: {func.__name__} failed: {e}"
                logger.error(err_msg)
                raise e
        return wrapper
    return decorator