# Wisielec

1) W tablicy znajdują się "narysowane" obrazki wisielca.
2) Do pliku "hasla.txt" zapisywane są różne przysłowia, które będą losowane i używane w grze.
3) Gdy skrypt zostaje uruchomiony, w konsoli pojawia się jedno losowe hasło z pliku "hasla.txt" zastępione odpowiednią ilością znaków podłogi "_" (spacje i przecinki, jeśli znajdują się w haśle, pozostają bez zmian) oraz pierwszy, startowy obrazek wisielca z tablicy.
4) Następnie skrypt wymaga od użytkownika podania jednej literki (dozwolone polskie znaki), obojętnie czy wprowadzonej z małej czy z dużej litery.
5) Jeśli użytkownik trafi literkę, która znajduje się w haśle, zamiast znaków podłogi w ich miejscu pojawia się odgadnięta literka. W przeciwnym razie (jeśli użytkownik nie trafi literki) zostaje wyświetlony kolejny obrazek wisielca, a pod nim hasło (z podłogami lub ogadniętymi literkami), i tak w kółko.
6) Gra kończy się, gdy zostanie wyświetlony ostatni obrazek wisielca - w tej sytuacji w konsoli wyskoczy komunikat z informacją o przegranej. Gracz wygrywa grę, jeśli odgadnie wszystkie literki z hasła - w tej sytuacji również wyświetli się odpowiedni komunikat.