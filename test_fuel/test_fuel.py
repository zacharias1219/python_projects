import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("5/1")