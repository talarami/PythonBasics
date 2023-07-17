# zadanie: Liczby nieparzyste dodane do set. Dodaj listę numList z wartościami od -4 do 4 z krokiem
#co 1. Ddoaj set z wartością początkową -2. Stówrz pętlę for przechodzącą po numList. W każdej
# iteracji pętli sprawdź czy liczba z listy jest nieparzysta czyli reszta z dzielenia przez 2
# nie może być równa 0. Dodaj nieparzystą liczbę do zestawu. Wyświetl w konsoli nieparzyste liczby
# w set za pomocą pętli for.

numList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

numList.append(1)
numList.append(2)
numList.append(3)

tripledSet = {-12}

for num in numList:
    tripledSet.add(num * 3)
    
for value in tripledSet:
    print(value)
