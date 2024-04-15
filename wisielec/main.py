# Wisielec
import random

# Obrazki wisielca w tablicy
wisielec = [
    """+-------
|/    |
|     O
|    /|\\
|    / \\
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
|     |
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
|     
|     
|     
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


# Losowanie hasła
def losuj_haslo():
    wylosowane_haslo = hasla[random.randint(0, len(hasla) - 1)]
    for i in wylosowane_haslo:
        znaki_w_hasle.append(i)
    for i in znaki_w_hasle:
        if (i.isalpha()):  # Sprawdzanie, czy znak jest literą
            znaki_na_podlogi.append("_")
        else:
            znaki_na_podlogi.append(i)
    for i in znaki_na_podlogi:
        print(i, end="")


losuj_haslo()
print()


# Trafianie liter przez gracza
tura = 1
def trafianieLiter():
    global tura
    literka = input(f"Podaj {tura}. literę: ").lower()
    while (literka.isalpha() == False):
        literka = input(f"Błąd!\nNie podano litery.\nPodaj {tura}. literę: ").lower()
    while (len(literka) > 1):
        literka = input(f"Błąd!\nPodano więcej niż jeden znak.\nPodaj {tura}. literę: ").lower()
    tura += 1
    if literka in znaki_w_hasle:
        odgadnieta_literka_index = znaki_w_hasle.index(literka)
        znaki_na_podlogi[odgadnieta_literka_index] = literka
    else:
        print(f"Literka '{literka}' nie znajduje się w haśle!")
    print()
    for i in znaki_na_podlogi:
        print(i, end="")
    print()
    trafianieLiter()

trafianieLiter()
