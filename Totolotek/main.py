# Symulacja losowania totolotka

import random
import math

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