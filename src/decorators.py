from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    def decorator(func: Any):
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                output_massage = f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}'
                raise e
            else:
                output_massage = f'{func.__name__} ok'
                return result
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f'{output_massage}\n')
                else:
                    print(output_massage)
        return inner
    return decorator

if __name__ == '__main__':

    @log()
    def my_function(x, y):
        return x / y

    print(my_function(1, 2))
    print(my_function(1, 2))
    # print(my_function(1, 0))
