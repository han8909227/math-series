"""A group of mathematical sum series functions."""


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
    """Find the nth value in a sum series.

    Optional arguments are the 1st and 2nd numbers in that series.
    """
    if n == 0:
        return num1

    if n == 1:
        return num2

    return sum_series((n - 1), num1, num2) + sum_series((n - 2), num1, num2)

if __name__ == '__main__':
    print(__doc__)
    print('fibonacci(n):\n\t%s' % fibonacci.__doc__)
    for n in range(5):
        print('>>> fibonacci(%i)' % n)
        print(fibonacci(n))
    print('lucas(n):\n\t%s' % lucas.__doc__)
    for n in range(5):
        print('>>> lucas(%i)' % n)
        print(lucas(n))
    print('sum_series(n):\n\t%s' % sum_series.__doc__)
    for n in range(5):
        print('>>> sum_series(%i)' % n)
        print(sum_series(n))
    for n in range(5):
        print('>>> sum_series(%i, 2, 1)' % n)
        print(sum_series(n, 2, 1))
    for n in range(5):
        print('>>> sum_series(%i, 6, 8)' % n)
        print(sum_series(n, 6, 8))
