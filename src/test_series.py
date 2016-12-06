"""This is the test for the fibonacci and lucas number series in series.py."""
import pytest

# Expected answers for Fibonacci sequence.
PARAMS_FIB = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2)
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