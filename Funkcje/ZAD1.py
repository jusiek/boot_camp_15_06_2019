def test_liczba_pierwsza (x):
    for i in range(2, x):
        if x % i == 0:
            return False
        return True

def test_czy_jest_pierwsza():
    assert  test_liczba_pierwsza(2) == True
    assert  test_liczba_pierwsza(3) == True
    assert  test_liczba_pierwsza(11) == True

def test_czy_nie_jest_pierwsza():
    assert  test_liczba_pierwsza(2) == False
    assert  test_liczba_pierwsza(3) == False
    assert  test_liczba_pierwsza(11) == False