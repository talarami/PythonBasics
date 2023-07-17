
# prosta konwersja

import math
import random

print( type(str( 12 )) ) # konwersja liczby całkowitej na łańcuch znaków, w konsoli: <class 'str'>
print( type(str( [12, 34] )) ) # w konsoli: <class 'str'>

number = int("123") # konwersja na liczby 
print(type(number)) # w konsoli: <class 'int'>, dopiero teraz można przeprowadzać działania matematyczne, na łańcuchu znaków jest to niemożliwe

number += 10
print(number) # w konsoli: 133
print( "123" + "10") # w konsoli: 12310 - łańcuch znaków

floatNum = float("45.67")  # konwersja łańcuchu znaków na float
print(type(floatNum)) # w konsoli: <class 'float'>
floatNum = floatNum * 2 # możliwe wykonanie operacji matematycznych 
print(floatNum) # w konsoli: 91.34

# wartość bezwzględna:

print(abs(9)) # w konsoli: 9
print(abs(-9.1)) # w konsoli: 9.1

# zaokrąglenie do liczby całkowitej nie mniejszej niż podana (do góry):

print(math.ceil(11.000001)) # w konsoli: 12
print(math.ceil(9.99999)) # w konsoli: 10
print(math.ceil(-1.00001)) # w konsoli: -1

# zaokrąglenie do liczby całkowitej nie większej niż podana (do dołu):

print(math.floor(11.000001)) # 11
print(math.floor(11.99999)) # 11
print(math.floor(-5.12)) # -6
print(math.floor(-5.99999)) # -6

# uzyskanie informacji o największej liczbie z przekazanych wartości:

print(max(10, 1, -9, 33, 89, 0)) # 89 
print(max( [10, 1, -9, 33, 89, 0] )) # 89
print(max((10, 1, -9, 33, 89, 0))) # 89

# uzyskanie informacji o najmniejszej liczbie z przekazanych wartości:

print(min(10, 1, -9, 33, 89, 0)) # -9
print(min( [10, 1, -9, 33, 89, 0] )) # -9
print(min((10, 1, -9, 33, 89, 0))) # -9

# podnoszenie do potęgi:

print( 4 ** 3 ) # 64
print( pow(4, 3)) # 64

# pierwiastek kwadratowyz jakiejś liczby:

print(math.sqrt(128)) # 11.313708498984761

# zaokrąglanie liczby do określonej ilości miejsc po przecinku:

print(round(12.789029342, 3)) # 12.789
print(round(12.789029342, 2)) # 12.79
print(round(12.789029342, 1)) # 12.8

# losowe elementy:

print( random.random() ) # np. 0.009915129768999442
print( random.random() * 100 ) # np. 87.65548517644002
print( int(random.random() * 100)) # np. 23

print( random.choice( [0, 1, 2, 3, 4] ) ) # np. 1
print( random.choice( ["Ola", "Ania", "Adam"] ) ) # np. Ania

# losowa wartość z zakresu, od -10, do 30, z krokiem co 5:

print( random.randrange(-10, 30, 5)) # np. 15

# ustawienie elementów z listy w losowej kolejności:

listData = [0, 1, 2, 3, 4, 5, 6]

random.shuffle(listData)

print(listData) # np. [3, 2, 6, 4, 1, 0, 5]

      

















