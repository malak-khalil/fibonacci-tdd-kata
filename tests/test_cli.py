"""Tests for the Fibonacci command-line interface."""

import pytest

from fibonacci_tdd_kata.cli import build_parser, main


def test_parser_accepts_single_number() -> None:
    args = build_parser().parse_args(["10"])
    assert args.n == 10


def test_parser_accepts_range() -> None:
    args = build_parser().parse_args(["--start", "0", "--end", "5"])
    assert args.start == 0
    assert args.end == 5


def test_main_prints_single_value(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "10"])
    main()
    assert capsys.readouterr().out.strip() == "55"


def test_main_prints_range(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "0", "--end", "5"],
    )
    main()
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["0", "1", "1", "2", "3", "5"]


def test_main_requires_an_argument(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("sys.argv", ["fibonacci-kata"])
    with pytest.raises(SystemExit):
        main()


def test_main_rejects_negative_number(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "-1"])
    with pytest.raises(SystemExit):
        main()


def test_main_requires_both_range_arguments(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("sys.argv", ["fibonacci-kata", "--start", "0"])
    with pytest.raises(SystemExit):
        main()


def test_main_rejects_invalid_range(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["fibonacci-kata", "--start", "5", "--end", "0"],
    )
    with pytest.raises(SystemExit):
        main()
