from bank import value

def test_greetings():
    assert value("hello?") == 0
    assert value("HELLO!!") == 0
    assert value("HEY") == 20
    assert value("how are ya?") == 20
    assert value("What's up") == 100
    assert value("What brings you here?") == 100