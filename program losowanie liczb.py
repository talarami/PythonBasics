import random

def drawNumber(start, end):
    return random.randint(start, end)


start = int(input("Wprowadź dolną granicę zakresu liczba całkowita: ")) # np. 1
end = int(input("Wprowadź góną granicę zakresu, liczba całkowita: ")) # np. 100
drawCount = int(input("Ile liczb ma być wylosowanych: "))

if start >= end or drawCount <= 0 or (end - start + 1) < drawCount:
    print("Błędne dane wyjściowe")
else:
    drawnNumbers = set()
    while len(drawnNumbers) < drawCount:
        drawnNumbers.add( drawNumber(start, end) )

print("Wyniki: " + str(drawnNumbers)) # np. Wyniki: {68, 37, 79, 57, 90}

