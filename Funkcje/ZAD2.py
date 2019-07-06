def czy_litera_wiecej_niz(litera, napis, prog):
    if napis.count(litera) > prog:
        return True
    return False


def wiecej_niz(napis, prog):
    zbior_wynikowy = set()
    for litera in napis:
        if napis.count(litera) > prog:
            zbior_wynikowy.add(litera)
        return zbior_wynikowy


def test_wiecej_niz_z_napisem_i_progiem():
    assert wiecej_niz("a","aaaa", 3) == {'a'}


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("", 0) == set()
