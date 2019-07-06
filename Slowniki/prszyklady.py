osoba = {

    "imie": "Rafał",
    "nazwisko": "Jusiek",
    "hobby": ["muzyka","historyka","..."],
    "dzieci": {"corka1":"Gabriela"}
}

dzieci = osoba['dzieci']
dzieci["corka1"] = "Gabi"
print(osoba)

osoba["sport"] = ["armwrestling"]
print(osoba)

print(osoba.get("zona", "brak"))

print(osoba.keys())

print(dir(osoba))

print(osoba.pop())
print(osoba)