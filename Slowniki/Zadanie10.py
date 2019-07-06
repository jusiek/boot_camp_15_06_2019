napis = input("Podaj słowo ")
liczniki = {}
for l in napis:
    if l in liczniki:
        liczniki[l] += 1
    else:
        liczniki[l] = 1

print(liczniki)