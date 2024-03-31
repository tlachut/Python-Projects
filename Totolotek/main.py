# Symulacja losowania totolotka

import random

# Losowanie liczb komputera

wylosowaneLiczby = []

def sprawdzCzyWystepujePowtorkaKomputer():
    wylosowanaLiczba = random.randint(1, 49)
    if wylosowanaLiczba not in wylosowaneLiczby:
        wylosowaneLiczby.append(wylosowanaLiczba)
    else: sprawdzCzyWystepujePowtorkaKomputer()

for i in range(6):
    sprawdzCzyWystepujePowtorkaKomputer()