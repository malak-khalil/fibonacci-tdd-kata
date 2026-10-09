# /// script
# requires-python = ">=3.12"
# dependencies = ["marimo", "matplotlib"]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt

    import micropip

    await micropip.install("fibonacci-tdd-kataa==0.1.0")

    from fibonacci_tdd_kata import fibonacci


@app.cell
def _():
    mo.md("""
    # Fibonacci Explorer

    Explore the Fibonacci sequence using interactive sliders.

    This notebook imports `fibonacci` from the installed
    `fibonacci_tdd_kata` package. It does not reimplement it.
    """)
    return


@app.cell
def _():
    n = mo.ui.slider(
        start=0,
        stop=30,
        step=1,
        value=10,
        label="Fibonacci index (n)",
    )

    count = mo.ui.slider(
        start=5,
        stop=30,
        step=1,
        value=15,
        label="Number of sequence values",
    )

    mo.vstack([n, count])
    return count, n


@app.cell
def _(n):
    mo.md(f"""
    **F({n.value}) = {fibonacci(n.value)}**
    """)
    return


@app.cell
def _(count):
    indices = list(range(count.value))
    values = [fibonacci(i) for i in indices]

    mo.md(f"**First {count.value} Fibonacci numbers:**")
    mo.md(str(values))
    return indices, values


@app.cell
def _(indices, values):
    fig, ax = plt.subplots(figsize=(9, 4))

    ax.bar(indices, values, color="#4c72b0")
    ax.set_xlabel("Index (n)")
    ax.set_ylabel("Fibonacci number F(n)")
    ax.set_title("Fibonacci Sequence")
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    fig
    return


if __name__ == "__main__":
    app.run()
