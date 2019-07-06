def policz_znaki("Ala ma <kota> a kot ma ale"):
    return

def test_policz_znaki():
    assert policz_znaki(4) == 4
    assert policz_znaki(3) == 9
    assert policz_znaki(2, 3) == 8
    assert policz_znaki(3, 3) == 27


def test_policz_znaki():
    assert policz_znaki("a","aaaa", 3) == {'a'}