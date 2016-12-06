"""This code houses the Fibonacci and Lucas functions."""


def fibonacci(n):
    """Return the nth term of the fibonacci sequence."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return the nth term of the Lucas sequence."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, x=0, y=1):
    """Return the nth term of a customizable series with base cases
    n == 0 return x and n == 1 return y. Returns the nth term of the
    Fibonacci series if no optional parameters entered."""
    if n == 0:
        return x
    if n == 1:
        return y
    else:
        return sum_series(n-2, x, y) + sum_series(n-1, x, y)