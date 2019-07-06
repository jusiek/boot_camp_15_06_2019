slowo = "python"

wynik = ["_" for x in slowo]
szanse = len(slowo) + 3
print(slowo)
print(wynik)

while True:
    znak = input("Wprowadz znak: ")

    if znak not in slowo:
        szanse -= 1
    if szanse == 0:
        print("przegrałes")
        break

    i = 0
    for litera in slowo:
        if znak == litera:
            wynik[i] = znak
        i += 1
    if "".join(wynik) == slowo:
        print("wygrales")
        break
    else:
        print(f"pozostalo szans: {szanse}")
    print("".join(wynik))