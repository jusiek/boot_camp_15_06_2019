format = {'koszt $cena PLN',
          'kwota $cena brutto',
          'cena = 10'
          }
mapowanie = {'a':'c'}

def test_zmiana():
    for cena in kwargs:
        print(f"zmieniam {cena} na {cena, kwargs[cena]}")
        cena = cena.replace(cena, kwargs[cena])
    return cena

