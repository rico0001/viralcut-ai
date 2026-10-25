from typing import Callable, Any
import time

def retry(func: Callable[..., Any], retries: int = 3, delay: float = 1.0) -> Any:
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e