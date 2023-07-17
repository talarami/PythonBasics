# Podstawą pracy z danymi jest konwersja między jednym typem a drugim np z str na int.

string = str(12.56)
print(type(string)) # w konsoli: <class 'str'>

listData = str( [0,1, 2, 3] )
print(type(listData)) # w konsoli: <class 'str'>

number = int("68")
print(type(number)) # w konsoli: <class 'int'>

number2 = float ("20.03")
print(type(number2)) # w konsoli: <class 'float'>

# funkcje matematyczne

import math

# wartość bezwzględna:

print(abs(5)) # 5
print(abs(-5)) # 5

# zaokrąglenie do najmniejszej liczby całkowitej nie mniejszej niż podana wartość:

print(math.ceil(6.78)) # 7
print(math.ceil(20.12)) # 21
print(math.ceil(-3.23)) # -3

# zaokrąglenie do największej liczby całkowitej nie większej niż podana wartość:

print(math.floor(6.78)) # 3
print(math.floor(20.12)) # 20
print(math.floor(-3.23)) # -4

# max zwróci największą wartość z przekazanych:

print(max(12, 3, 78, 32, 11)) # 78
print(max([9, 67, 43, -2])) # 67

# min zwróci najmniejszą wartość z przekazanych:

print(min(12, 3, 78, 32, 11)) # 3
print(min([9, 67, 43, -2])) # -2


print(pow(2, 3)) # potęgowanie, to samo co x**y, w konsoli: 8

print(math.sqrt(16)) # pierwiastkowanie, pierwiastek z 16, w konsoli: 4

print(round(23.12345, 3)) # zaokrąglenie do 3 miejsc po przecinku, w konsoli: 23.123


import random

# losowy float od 0 i mniejszy od 1 np 0.92:

print(random.random())

# losowy element z listy, krotki lub str

print(random.choice([4, 3, 8])) # np. 3
print(random.choice(("Ola", "Ania", "Adam"))) # np. Adam

# losowy element z zakresu: start, stop, step:

print(random.randrange(0, 25, 5)) # np. 10

# ustawia losowo elementy listy:

listData = [0, 1, 2, 3, 4]
random.shuffle(listData)
print(listData) # np. [1, 3, 4, 0, 2]

# losowy float większy od x i mniejszy od y:

print(random.uniform(2.3, 10.78)) # np. 3.5340559333026604

# Dodatkowo python oferuje wiele funkcji trygonometrycznych jak acos(), asin(), atan(), cos() itd.







