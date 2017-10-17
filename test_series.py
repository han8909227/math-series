"""Test for series functions."""
import pytest


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
def test_sum(n, result):
    """Test the sum series function for correct output"""
    import series
    assert series.sum_series(n) == result


SUM_SERIES = [(x, 2, 1, y) for x, y in LUCAS_NUMS]


@pytest.mark.parametrize('n, num1, num2, result', SUM_SERIES)
def test_sum_lucas(n, num1, num2, result):
    """Test the sum series"""
    import series
    assert series.sum_series(n, num1, num2) == result
