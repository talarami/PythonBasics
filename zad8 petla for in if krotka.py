# zadanie: Wyświetlanie nieparzystych licz z krotki. Stwórz krotkę z wartościami od 1 do 10.
# Zrób pętlę for in z krotką i wyświetl w konsoli tylko nieparzyste liczby. Skorzystaj z instrukcji
# warunkowej if oraz operatora % zwracającego resztę z dzielenia. Jeśli reszta z dzielenia
# przez 2 będzie równa 1 to liczba jest nieparzysta.

data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for v in data:
    print(data[: : 2])
    

for v in data:
    if v % 2 == 1:
        print(v, "to liczba nieparzysta")