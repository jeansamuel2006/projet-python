import pytest

from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(x, y):
        return x + y

    add(1, 2)
    captured = capsys.readouterr()  # capture la sortie console
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_success_file(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    multiply(2, 3)
    assert "multiply ok" in log_file.read_text(encoding="utf-8")
