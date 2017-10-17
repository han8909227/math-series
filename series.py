"""A group of sum series functions"""


def fibonacci(n):
    """Find the nth value in the Fibonacci Series."""
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Find the nth value in the Lucas Numbers series."""
    if n == 0:
        return 2

    if n == 1:
        return 1

    num1 = 2
    num2 = 1
    for _ in range(n - 1):
        num1, num2 = num2, num1 + num2
    return num2


def sum_series(n, num1=0, num2=1):
    """Find the nth value in a sum series
    given 1st and 2nd number in that series"""
    if n == 0:
        return num1

    if n == 1:
        return num2

    return sum_series((n - 1), num1, num2) + sum_series((n - 2), num1, num2)
