"""Test for series functions"""
import pytest

@pytest.mark.parametrize('n,result',[(1,0),(2,1),(3,1),(4,2),(5,3),(6,5),(7,8),(8,13)])

def test_fib(n,result):
    import series
    assert series.fibonacci(n) == result


