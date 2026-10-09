import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Fibonacci TDD Kata

    ## Objective

    This notebook demonstrates the Test-Driven Development workflow by implementing
    the Fibonacci sequence step by step.

    ## Fibonacci sequence

    The sequence is defined as:

    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n - 1) + F(n - 2) for n >= 2

    ## TDD workflow

    The implementation follows the Red → Green → Refactor cycle:

    1. Write tests that initially fail.
    2. Implement the function until all tests pass.
    3. Refactor the code while keeping the test suite green.

    ## Interactive demo

    Use the widget below to select a value of `n` and display the corresponding
    Fibonacci number.
    """)
    return


@app.function
def fibonacci(n):
    def fib_pair(k):
        if k == 0:
            return 0, 1

        a, b = fib_pair(k // 2)

        c = a * (2 * b - a)
        d = a * a + b * b

        if k % 2 == 0:
            return c, d
        return d, c + d

    return fib_pair(n)[0]


@app.cell
def _():
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

    return


@app.cell
def _(mo):
    n_input = mo.ui.number(
        start=0,
        stop=30,
        step=1,
        value=10,
        label="n"
    )

    n_input
    return (n_input,)


@app.cell
def _(mo, n_input):
    mo.md(
        f"**F({n_input.value}) = {fibonacci(n_input.value)}**"
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ## Large-value tests

    These tests serve two purposes:

    1. **Correctness after optimization**
       We verify that the function still returns known Fibonacci values for larger inputs.

    2. **Performance motivation**
       We use a much larger input to reveal the limitations of the naive recursive implementation
       before refactoring it for better performance.
    """)
    return


@app.function
def test_fibonacci_large_values():
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040


@app.function
def test_fibonacci_large_recurrence():
    n = 1000
    assert fibonacci(n) == fibonacci(n - 1) + fibonacci(n - 2)


@app.function
# Large-scale performance and correctness test:
# Verifies that the optimized implementation can handle n = 10^7.
# Two consecutive Fibonacci numbers are always coprime.
def test_fibonacci_very_large():
    import math

    n = 10**7
    fn = fibonacci(n)
    fn_next = fibonacci(n + 1)

    assert math.gcd(fn, fn_next) == 1


if __name__ == "__main__":
    app.run()
