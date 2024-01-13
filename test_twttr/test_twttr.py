from twttr import shorten


def test_assert():
    assert shorten("h3ll0 w@rld") == "h3ll0 w@rld"
    assert shorten("array") == "rry"
    assert shorten("Richard!!!") == "Rchrd!!!"
    assert shorten("EMPTY") == "MPTY"