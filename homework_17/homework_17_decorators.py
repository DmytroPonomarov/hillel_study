"""
Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
"""


def logg(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log = f"Function: {func.__name__}, input data: {args}, {kwargs}, result: {result}\n"
        with open("homework_17_1_log.txt", "a") as file:
            file.write(log)
        return result

    return wrapper


@logg
def sumtwo_first(a, b):
    sum_result = a + b
    return sum_result


def logg_exc(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            log = f"Function: {func.__name__}, error: {type(e).__name__}, input data: {args}, {kwargs}\n"
            with open("homework_17_2_log.txt", "a") as file:
                file.write(log)

    return wrapper


@logg_exc
def sumtwo_second(a, b):
    sum_result = a + b
    return sum_result


if __name__ == "__main__":
    sumtwo_first(10, 20)
    sumtwo_second("test", 20)
