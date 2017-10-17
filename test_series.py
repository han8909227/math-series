"""Test for series functions."""
import pytest


FIB_NUMS = [(1, 0), (2, 1), (3, 1), (4, 2), (5, 3), (6, 5), (7, 8), (8, 13)]


@pytest.mark.parametrize('n,result', FIB_NUMS)
def test_fib(n, result):
    import series
    assert series.fibonacci(n) == result


LUCAS_NUMS = [(0, 2), (1, 1)]
for n in range(2, 100):
    LUCAS_NUMS.append((n, LUCAS_NUMS[-2][1] + LUCAS_NUMS[-1][1]))


@pytest.mark.parametrize('n,result', LUCAS_NUMS)
def test_lucas(n, result):
    """Test the lucas function in the series module for proper output."""
    import series
    assert series.lucas(n) == result
