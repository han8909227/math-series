"""Test for the series module functions."""
import pytest
from random import randint


FIB_NUMS = [(0, 0), (1, 1)]
for n in range(2, 20):
    FIB_NUMS.append((n, FIB_NUMS[-2][1] + FIB_NUMS[-1][1]))


@pytest.mark.parametrize('n,result', FIB_NUMS)
def test_fib(n, result):
    """Test the fibonacci series for correct output."""
    import series
    assert series.fibonacci(n) == result


LUCAS_NUMS = [(0, 2), (1, 1)]
for n in range(2, 20):
    LUCAS_NUMS.append((n, LUCAS_NUMS[-2][1] + LUCAS_NUMS[-1][1]))


@pytest.mark.parametrize('n,result', LUCAS_NUMS)
def test_lucas(n, result):
    """Test the lucas function in the series module for proper output."""
    import series
    assert series.lucas(n) == result

SUM_SERIES = FIB_NUMS


@pytest.mark.parametrize('n,result', SUM_SERIES)
def test_sum_fib(n, result):
    """Test the sum_series function when given no additional arguments."""
    import series
    assert series.sum_series(n) == result


RAND_SUM_SERIES = [(x, 2, 1, y) for x, y in LUCAS_NUMS]  # Include Lucas Nums
for _ in range(10):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    sum_ser = [(0, num1, num2, num1), (1, num1, num2, num2)]
    for n in range(2, 20):
        sum_ser.append((n, num1, num2, sum_ser[-2][3] + sum_ser[-1][3]))
    RAND_SUM_SERIES.extend(sum_ser)


@pytest.mark.parametrize('n, num1, num2, result', sum_ser)
def test_sum_general(n, num1, num2, result):
    """Test the sum_series when given random starting numbers."""
    import series
    assert series.sum_series(n, num1, num2) == result
