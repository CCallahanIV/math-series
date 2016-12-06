"""This is the test for the fibonacci and lucas number series in series.py."""
import pytest

# Expected answers for Fibonacci sequence.
PARAMS_FIB = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),

]

# Expected answers for Lucas number sequence.
PARAMS_LUC = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18)
]

PARAMS_2_11 = [
    (0, 2),
    (1, 11),
    (2, 13),
    (3, 24),
    (4, 37),
    (5, 61),
]

@pytest.mark.parametrize("n, result", PARAMS_FIB)
def test_fibonacci(n, result):
    """Test the fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", PARAMS_LUC)
def test_lucas(n, result):
    """Test the lucas function."""
    from series import lucas
    assert lucas(n) == result

@pytest.mark.parametrize("n, result", PARAMS_FIB)
def test_sum_series_default(n, result):
    """Test the sum_series function with default values that should return fibonacci sequence"""
    from series import sum_series
    assert sum_series(n) == result

@pytest.mark.parametrize("n, result", PARAMS_LUC)
def test_sum_series_luc(n, result):
    """Test the sum_series function passing the lucas initial values (2 and 1) which should return the lucas sequence"""
    from series import sum_series
    assert sum_series(n, 2, 1) == result


@pytest.mark.parametrize("n, result", PARAMS_2_11)
def test_sum_series_2_11(n, result):
    """Test the sum_series function passing 2 and 11 as initial values."""
    from series import sum_series
    assert sum_series(n, 2, 11) == result