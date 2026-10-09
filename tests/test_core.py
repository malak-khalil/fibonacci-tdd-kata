"""Tests for the Fibonacci implementation."""

import math

import pytest

from fibonacci_tdd_kata.core import fibonacci


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_two():
    assert fibonacci(2) == 1


def test_fibonacci_three():
    assert fibonacci(3) == 2


def test_fibonacci_four():
    assert fibonacci(4) == 3


def test_fibonacci_five():
    assert fibonacci(5) == 5


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (10, 55),
        (20, 6765),
        (30, 832040),
    ],
)
def test_fibonacci_large_values(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_large_recurrence():
    n = 1000
    assert fibonacci(n) == fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci_very_large():
    n = 10**7
    fn = fibonacci(n)
    fn_next = fibonacci(n + 1)

    assert math.gcd(fn, fn_next) == 1


def test_fibonacci_negative_input():
    with pytest.raises(ValueError):
        fibonacci(-1)
