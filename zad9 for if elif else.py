# zadanie: Wyświetl w konsoli następujące informacje z użyciem pętli na liście oraz instrukcji
#if elif else w celu sprawdzenia czy liczba jest parzysta czy nieparzysta. Lista licz od -7 do 7.
# 0 jest oddzielnym przypadkiem.

dataList = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

for n in dataList:
    if n == 0:
        print(n, "to liczba parzysta")
    elif n % 2 == 0:
        print(n, "liczba parzysta")
    else:
        print(n, "to liczba nieparzysta")