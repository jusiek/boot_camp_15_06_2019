lista =  []

while len(lista) < 10:
    odp = input("Podaj liczbe ")
    if odp == "k":
        break
    liczba = int(odp)
    liczba.append(odp)
if len(liczba) > 0:
    srednia = sum(liczba / len(liczba))
    print(f"średnia z {liczba} wynosi {srednia}")