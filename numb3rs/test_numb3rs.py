from numb3rs import validate


def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("CS%)") == False
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("249.249.270.249") == False