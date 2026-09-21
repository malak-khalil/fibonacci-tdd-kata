import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest

    return


@app.cell
def _():
    # Fibonacci TDD with Marimo
    return


@app.function
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
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


if __name__ == "__main__":
    app.run()
