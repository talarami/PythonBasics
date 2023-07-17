
# Zadanie na Number: 
# 1) pobierz liczbę całkowitą od użytkownika do zmiennej za pomocą funkcji input, przekaż do niej informację: Podaj liczbę całkowitą.
# 2) Zmień typ wartości z tekstu na liczbę całkowitą.
# 3) Stwórz funkcję calculateSquareArea z parametrem height któa zwraca powierzchnię kwadrata.
# 4) Wywołaj funkcję z wcześniej pobraną liczbą całkowitą, pokaż wynik w konsoli.
# 5) Pobierz od użytkownika liczbę dziesiętną. Oblicz powierzchnię kwadratu z tą wartością, pokaż wynik w konsoli 
# zaokrąglony do 2 miejsc po przecinku.

intStr = input("Podaj liczbę całkowitą:")
intNumber = int(intStr)

def calculateSquareArea(height):
        return height * height

squareArea = calculateSquareArea(intNumber)

print("Powierzchnia kwadratu:", squareArea)


floatStr = input("Podaj liczbę dziesiętną:")
floatNumber = float(floatStr)

squareArea2 = calculateSquareArea(floatNumber)

print("Powierzchnia kwadratu:", squareArea2)

print(round(squareArea2, 2))

