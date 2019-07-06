print("Pomidor 2.5 Ziemniaki 4.5 Ogorki 5.5 Cebula 2.33")

produkty = {

    "Pomidor" : 2.5,
    "Ziemniaki" : 4.5,
    "Ogorki" : 5.5,
    "Cebula" : 2.33,
}

magazyn = {

    "Pomidor" : 40,
    "Ziemniaki" : 50,
    "Ogorki" : 90,
    "Cebula" : 22,
}



print("Nasz zieleniak oferuje: ")
for p in produkty:
    print(f" - {p}: {produkty[p]} PLN")

co = input("Co chcesz kupic? ")
ile = float(input(f"Ile chcesz kupić [{co}]?"))
if ile > magazyn[co]:
    print("Nie mam tyle produktu ")
else
koszt = ile * produkty[co]

print(f"Do zapłaty: {koszt:.2f}")
print(f"Magazyn: {magazyn}")