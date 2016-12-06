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
