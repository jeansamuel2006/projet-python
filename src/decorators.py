from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования начала, конца и ошибок функции."""

    def wrapper(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                log_message(message, filename)
                raise
            log_message(message, filename)
            return result

        return inner

    return wrapper


def log_message(message: str, filename: str | None) -> None:
    """Записывает сообщение в файл или выводит в консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)
