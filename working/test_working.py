import pytest as pt
from working import convert


def test_convert():
    assert convert("4 AM to 11 AM") == "04:00 to 11:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("10 AM to 8 PM") == "10:00 to 20:00"

def test_value_error():
    with pt.raises(ValueError):
        convert("9 - 5PM")
    with pt.raises(ValueError):
        convert("15:00 AM to 25:60 PM")