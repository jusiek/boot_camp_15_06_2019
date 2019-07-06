def policz_znaki(napis):
    licznik = 0
    poziom = 0
    for znak in napis:
        if znak == "<":
            poziom+= 1
            continue
        elif znak == ">":
            poziom -= 1
            continue
        licznik += poziom
        return


def test_policz_znaki_1_poziom():
    assert policz_znaki ('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki ('ala ma <kota> a kot ma ale') == 6

def test_policz_znaki_wiele_poziomow():
    assert policz_znaki('a <a<a>>>') == 6

def test_policz_znaki_wiele_poziomow_niestandardowe_znaki():
    assert policz_znaki('ala [kota[a kot]] ma [ale]') == 18

