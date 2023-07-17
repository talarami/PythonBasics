

# KONWERSJA NA INT

# konwersja float na int:
floatNumber = 12.3
intNumber = int(floatNumber)
print(intNumber) # w konsoli: 12


# KONWERSJA NA FLOAT

# konwersja int na float:
intNumber = 20
floatNumber = float(intNumber) 
print(floatNumber) # w konsoli: 20.0


# KONWERSJA NA ŁAŃCUCH ZNAKÓW (STRING)

# konwersja int na łańcuch znaków(string):
intNum = 10
str2 = str(intNum)
print(intNum) # w konsoli: 10


# KONWERSJA NA KROTKĘ (TUPLE)

# konwersja z listy na krotkę:
listData = [1, 2, 3, 4]
tupleData = tuple(listData)
print(type(tupleData)) # w konsoli: <class 'tuple'>


# KONWERSJA NA LISTĘ

# konwersja z krotki na listę:
tuple2 = ("Ola", "Adam")
newList = list(tuple2)
print(type(newList)) # w konsoli: <class 'list'>


# KONWERSJA NA SET

# konwersja na set, z listy na zbiór:
numberList = [4, 6, 8, 4, 6, 10, 12, 14]
uniqueSet = set(numberList)
print(type(uniqueSet)) # w konsoli: <class 'set'>


# KONWERSJA NA FROZENSET

# konwersja z listy na frozenset:
immutableset = frozenset(numberList)
print(type(immutableset)) # w konsoli: <class 'frozenset'>


# KONWERSJA NA SŁOWNIK

# konwersja z krotki na słownik:
contactTuples = (("Bob", "bob@example.com"), ("Ewa", "ewa@example.com"))
contactDict = dict(contactTuples)
print(contactDict)



