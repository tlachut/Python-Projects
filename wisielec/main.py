# Wisielec
import random

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


# Losowanie hasła
def losuj_haslo():
    wylosowane_haslo = hasla[random.randint(0, len(hasla) - 1)]
    znaki_w_hasle = []
    for i in wylosowane_haslo:
        znaki_w_hasle.append(i)
    znaki_na_podlogi = []
    for i in znaki_w_hasle:
        if (i.isalpha()):  # Sprawdzanie, czy znak jest literą
            znaki_na_podlogi.append("_")
        else:
            znaki_na_podlogi.append(i)
