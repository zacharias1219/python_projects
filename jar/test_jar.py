from jar import Jar

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(3)
    assert jar.size == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2