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
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


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


if __name__ == "__main__":
    app.run()
