from seasons import convert


def test_date():
    assert convert(730) == "One million, fifty-one thousand, two hundred minutes"
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
