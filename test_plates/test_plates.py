from plates import is_valid

def test_begintwoletters():
    assert is_valid("RI") == True
    assert is_valid("33") == False
    assert is_valid("R3IC") == False
    assert is_valid("3") == False


def test_length():
    assert is_valid("RICE21") == True
    assert is_valid("CS") == True
    assert is_valid("RICHARD19") == False


def test_num():
    assert is_valid("RIC321") == True
    assert is_valid("RIC30H") == False
    assert is_valid("RIC031") == False


def test_punct():
    assert is_valid("RICH!!") == False






