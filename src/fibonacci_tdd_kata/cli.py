"""Command-line interface for the Fibonacci TDD kata."""

import argparse

from fibonacci_tdd_kata import fibonacci


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="fibonacci-kata",
        description="Print a Fibonacci number or a range of Fibonacci numbers.",
    )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        help="A single Fibonacci index.",
    )
    parser.add_argument(
        "--start",
        type=int,
        help="Start of a range (inclusive).",
    )
    parser.add_argument(
        "--end",
        type=int,
        help="End of a range (inclusive).",
    )
    return parser


def main() -> None:
    """Run the Fibonacci command-line tool."""
    parser = build_parser()
    args = parser.parse_args()

    if args.start is not None and args.end is not None:
        if args.start < 0 or args.end < args.start:
            parser.error("Provide a non-negative range with start <= end.")
        for i in range(args.start, args.end + 1):
            print(fibonacci(i))
    elif args.start is not None or args.end is not None:
        parser.error("Provide both --start and --end.")
    elif args.n is not None:
        if args.n < 0:
            parser.error("n must be non-negative.")
        print(fibonacci(args.n))
    else:
        parser.error("Provide either a single number, or --start and --end.")


if __name__ == "__main__":
    main()
