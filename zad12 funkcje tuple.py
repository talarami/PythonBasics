# zadanie
# Stwórz krotkę z wartościami od -2 do 5. Napisz funkcję sumData(tuple) która zsumuje zawartość
# krotki i zwróć za pomocą return tąsumę. Wywołaj funkcję na krotce i pokaż wynik.

data = (-2, -1, 0, 1, 2, 3, 4, 5)

def sumData(tuple):
    sum = 0
    for num in tuple:
        sum += num

    return sum

result = sumData(data)
print("Suma elementów:", result)