"""Core Fibonacci implementation."""


def fibonacci(n: int) -> int:
    """Return F(n) using the fast-doubling algorithm."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    def fib_pair(k: int) -> tuple[int, int]:
        if k == 0:
            return 0, 1

        a, b = fib_pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b

        if k % 2 == 0:
            return c, d
        return d, c + d

    return fib_pair(n)[0]
