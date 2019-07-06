liczby_parzyste_0_100 = set(range(0, 100, 2))

liczby = set()
while True:
    komenda = input("Podaj komende lub k by zakonczyc ")
    if komenda == 'k':
        break
    else:
            liczby.add(int(komenda))

print(f"Liczby parzystych od 0 do 100 było: {len(liczby & liczby_parzyste_0_100)}")