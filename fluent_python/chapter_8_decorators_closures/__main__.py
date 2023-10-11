import time
from .clockdeco import clock
from .clockdecocls import clock as Clock
from functools import cache

registry = []


def register(func):
    print(f"Running register({func})")
    registry.append(func)
    return func


@register
def f1():
    print(f"Running f1()")


@register
def f2():
    print(f"Running f2()")


def f3():
    print(f"Running f3()")


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def even_better_make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


@Clock()
def snooze(seconds):
    time.sleep(seconds)


@Clock()
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@cache
@Clock()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def main():
    print(f"Running main()")
    print(f"Registry -> {registry}")
    f1()
    f2()
    f3()

    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(15))
    print(avg(26))

    avg_2 = even_better_make_averager()
    print(avg_2(10))
    print(avg_2(11))
    print(avg_2(15))
    print(avg_2(26))

    print("*" * 40, "Calling snooze(.123)")
    snooze(0.123)
    print("*" * 40, "Calling factorial(6)")
    print("6! = ", factorial(6))
    print("*" * 40, "Calling fibonacci(6)")
    print("fibonacci(60) = ", fibonacci(60))


if __name__ == "__main__":
    main()
