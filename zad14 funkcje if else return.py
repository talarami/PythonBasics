# zadanie
# Napisz program, który stworzy funkcję do porównania dwóch liczb. Stórz funkcję findSmallest, któa
# przyjmuje dwie liczby jako parametry (num1, num2). Funkcja musi pokazać w konsoli informację, która
# liczba jest mniejsza oraz jej wartość, np. "num1 jako 3 jest mniejsze niż num2 o wartości 5" lub
# że obie liczby są równe. Użyj if, elif, else. Dodatkowo funkcja zwraca mniejszą liczbę dzięki return.
# Sprawdź funkcję pokazując wartości 3 i 10, pokaż zwróconą wartość z funkcji. W ten sam sposób
# sprawdź funkcję dla 12 i 7.

def findSmallest(num1, num2):
    if num1 < num2:
        print("Num1 jako", num1, "jest mniejsze od num2 jako", num2)
        return num1
    elif num2 < num1:
        print("Num2 jako", num2, "jest mniejsze od num1 jako", num1)
        return num2
    else:
        print("Liczby są równe, mają wartość:", num1)
        return num1

    
print(findSmallest(3, 10))
print(findSmallest(12,7)) 