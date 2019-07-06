def sumator(*atgs):
    print(atgs)
    return sum(args)

def test_sumator():
    assert sumator(1) == 1
    assert sumator(1, 1) == 2
    assert sumator(1, 1, 5, 6, 7) == 20
    assert sumator(1, 1, 5, 6, 7, 8) == 28
    assert sumator(1, 1, 5 ,6 ,7, 8, 10) == 38