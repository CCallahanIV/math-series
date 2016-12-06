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

]

@pytest.mark.parametrize("n, result", PARAMS_FIB)
def test_fibonacci(n, result):
    """Test the fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result
