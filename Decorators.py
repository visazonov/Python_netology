import time
import datetime
import os
from functools import wraps


def logger(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        name = (
            f"Вызываем функцию {new_function.__name__} c аргументами {args} и {kwargs}"
        )
        result = old_function(*args, **kwargs)
        with open("data_package/main.log", "a", encoding="utf-8") as f:
            f.write(
                f"""
{start} {name}
Результат: {result}')
            """
            )
        return result

    return new_function


def test_1():
    path = "data_package/main.log"
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return "Hello World"

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert "Hello World" == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), "Должно вернуться целое число"
    assert result == 4, "2 + 2 = 4"
    result = div(6, 2)
    assert result == 3, "6 / 2 = 3"

    assert os.path.exists(path), "файл main.log должен существовать"

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert "summator" in log_file_content, "должно записаться имя функции"
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f"{item} должен быть записан в файл"


def logger_v2(path):
    def _logger_v2(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            name = f"Вызываем функцию {new_function.__name__} c аргументами {args} и {kwargs}"
            result = old_function(*args, **kwargs)
            with open(path, "a", encoding="utf-8") as f:
                f.write(
                    f"""
{datetime.datetime.now()} Вызываем функцию {new_function.__name__} c аргументами {args} и {kwargs}
Результат: {result}')
                """
                )
            return result

        return new_function

    return _logger_v2


def test_2():
    paths = ("log_1.log", "log_2.log", "log_3.log")

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger_v2(path)
        def hello_world():
            return "Hello World"

        @logger_v2(path)
        def summator(a, b=0):
            return a + b

        @logger_v2(path)
        def div(a, b):
            return a / b

        assert "Hello World" == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), "Должно вернуться целое число"
        assert result == 4, "2 + 2 = 4"
        result = div(6, 2)
        assert result == 3, "6 / 2 = 3"
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f"файл {path} должен существовать"

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert "summator" in log_file_content, "должно записаться имя функции"

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f"{item} должен быть записан в файл"


if __name__ == "__main__":
    test_1()
    test_2()
