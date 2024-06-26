# Symulacja losowania totolotka

import random
import datetime

# Losowanie liczb komputera

wylosowaneLiczby = []

def sprawdzPoprawnoscKomputer():
    wylosowanaLiczba = random.randint(1, 49)
    if wylosowanaLiczba not in wylosowaneLiczby:
        wylosowaneLiczby.append(wylosowanaLiczba)
    else: sprawdzPoprawnoscKomputer()

for i in range(6):
    sprawdzPoprawnoscKomputer()

# Wprowadzanie liczb przez użytkownika

liczbyUzytkownika = []

def sprawdzPoprawnoscUzytkownik():
    wprowadzonaLiczba = int(input(f"Wprowadź {i+1}. liczbę: "))
    if wprowadzonaLiczba not in liczbyUzytkownika and wprowadzonaLiczba <= 49 and wprowadzonaLiczba >= 1:
        liczbyUzytkownika.append(wprowadzonaLiczba)
    else:
        print("Błąd!")
        sprawdzPoprawnoscUzytkownik()

for i in range(6):
    sprawdzPoprawnoscUzytkownik()

# Trafione liczby

trafioneLiczby = []

for i in range(6):
    if liczbyUzytkownika[i] in wylosowaneLiczby:
        trafioneLiczby.append(liczbyUzytkownika[i])

# Wypisanie liczb w konsoli

print("|=====================================================|")
print("Liczby wprowadzone przez użytkownika to: ")
print(liczbyUzytkownika)
print("Liczby wylosowane przez program to: ")
print(wylosowaneLiczby)
print(f"Trafiono {len(trafioneLiczby)} liczb(ę/y): ")
print(trafioneLiczby)

# Dodanie dzisiejszej daty oraz licz do pliku

f = open("totolotek.txt", "a")
f.write(str(datetime.datetime.now()) + "\n")
f.write("Podane liczby: " + str(liczbyUzytkownika) + "\n")
f.write("Wylosowane liczby: " + str(wylosowaneLiczby) + "\n")
f.write("Trafione liczby: " + str(trafioneLiczby) + "\n\n")
