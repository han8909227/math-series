"""Series functions."""


def fibonacci(n):
    if n == 1:
        return 0

    if n == 2:
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
