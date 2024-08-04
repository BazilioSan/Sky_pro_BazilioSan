from functools import wraps
from typing import Any, Callable


def log(filename="") -> Callable:
    """Логирует в файл или консоль вызов функций-обработчиков и результаты их работы"""

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                message_ok = f"{function.__name__} ok"
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{message_ok}\n")
                else:
                    print(f"{message_ok}")
                return result
            except Exception as e:
                message_err = f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{message_err}\n")
                else:
                    print(f"{message_err}")

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y
