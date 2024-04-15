# Wisielec
import random

# Obrazki wisielca w tablicy
wisielec = [
"""+-------
|/    |
|     
|     
|     
|
+========""",
"""+-------
|/    |
|     O
|     
|     
|
+========""",
"""+-------
|/    |
|     O
|     |
|     
|
+========""",
"""+-------
|/    |
|     O
|    /|
|     
|
+========""",
"""+-------
|/    |
|     O
|    /|\\
|     
|
+========""",
"""+-------
|/    |
|     O
|    /|\\
|    / 
|
+========""",
"""+-------
|/    |
|     O
|    /|\\
|    / \\
|
+========""",
]

# Zapisywanie haseł do pliku
plik_hasla = open("hasla.txt", "w")
plik_hasla.write("""baba z wozu, koniom lżej
darowanemu słoniowi nie zagląda się w trąbę
czym się strułeś, tym się lecz
gdyby kózka nie skakała, toby nóżki nie złamała
czym chata bogata, tym rada
elektryka prąd nie tyka
wilk syty i owca cała
gąska kąska
cel uświęca środki
co dwie głowy, to nie jedna""")
plik_hasla.close()

# Wprowadzanie haseł z pliku do tabeli
plik_hasla = open("hasla.txt", "r")
hasla = []
for linia in plik_hasla:
    hasla.append(linia.strip())  # Usuwanie znaków nowej lini
plik_hasla.close()

znaki_na_podlogi = []
znaki_w_hasle = []

wylosowane_haslo = hasla[random.randint(0, len(hasla) - 1)]
# Losowanie hasła
def losuj_haslo():

    for i in wylosowane_haslo:
        znaki_w_hasle.append(i)
    for i in znaki_w_hasle:
        if (i.isalpha()):  # Sprawdzanie, czy znak jest literą
            znaki_na_podlogi.append("_")
        else:
            znaki_na_podlogi.append(i)
    print("Zaczynamy grę!")
    print(wisielec[0])
    for i in znaki_na_podlogi:
        print(i, end="")


losuj_haslo()
print()

# Trafianie liter przez gracza
tura = 1
proba = 1
wprowadzone_literki = []
def trafianieLiter():
    global tura
    global proba
    literka = input(f"Podaj {tura}. literę: ").lower()
    while (literka.isalpha() == False):
        literka = input(f"Błąd!\nNie podano litery.\nPodaj {tura}. literę: ").lower()
    while (len(literka) > 1):
        literka = input(f"Błąd!\nPodano więcej niż jeden znak.\nPodaj {tura}. literę: ").lower()
    while (literka in wprowadzone_literki):
        literka = input(f"Błąd!\nTa literka została już podana.\nPodaj {tura}. literę: ").lower()
    wprowadzone_literki.append(literka)
    tura += 1
    if literka in znaki_w_hasle:
        for n, i in enumerate(znaki_w_hasle):
            if i == literka:
                znaki_na_podlogi[n] = literka
    else:
        print(f"Literka '{literka}' nie znajduje się w haśle!")
        print(wisielec[proba])
        proba += 1
        if (proba == 7):
            exit(f"Przegrałeś!\nHasło to: '{wylosowane_haslo}'.")
    print()
    for i in znaki_na_podlogi:
        print(i, end="")
    print()
    if (znaki_w_hasle == znaki_na_podlogi):
        exit(f"Wygrałeś!\nHasło to: '{wylosowane_haslo}'.")
    trafianieLiter()

trafianieLiter()
