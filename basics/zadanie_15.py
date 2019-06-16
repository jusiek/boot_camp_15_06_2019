#AWSD
print("WITAJ NA PLANSZY")
import random
skarbx = (random.randint(0, 10))
skarby = (random.randint(0, 10))
graczx = (random.randint(0, 10))
graczy = (random.randint(0, 10))
wyjsciex = (random.randint (0, 10))
wyjsciey = (random.randint(0, 10))


while True:
    graczx = input(("Nakieruj wpisując AWSD: "))
    if graczx == 'A' or graczx == "a":
        print("Jesteś na pozycji" , graczx)
    elif graczx == 'W' or graczx == 'w':
        print("Jesteś na pozycji X")
    elif graczx == 'S' or graczx == 's':
        print("Jesteś na pozycji X")
    elif graczx == 'D' or graczx == 'd':
        print("Jesteś na pozycji X")
    else:
        print("Spadłeś poza mape")

while True:
    poz = input(("Nakieruj wpisując AWSD: "))
    if graczy == 'A' or graczy == "a":
        print("Jesteś na pozycji" , poz)
    elif poz == 'W' or poz == 'w':
        print("Jesteś na pozycji X")
    elif poz == 'S' or poz == 's':
        print("Jesteś na pozycji X")
    elif poz == 'D' or poz == 'd':
        print("Jesteś na pozycji X")
    else:
        print("Spadłeś poza mape")