

# Krotki w przeciwieństwie do listy są niemutowalne, jakakolwiek jej zmiana utworzy nową krotkę w pamięci.

tup1 = (0,1) + (2,3) + (4,) # konkatenacja; pojedyncza krotka z pojedycznym elementem musi występować w nawiasach okrągłych i z przecinkiem
print(tup1) # (0, 1, 2, 3, 4)
print(type(tup1)) # <class 'tuple'>

# zwielokrotnienie elementów:
print( (1,2) * 3 )

# sprawdzanie czy element istnieje w krotce:
print( 4 in tup1 )

# ilość elementów krotki:
print( len(tup1) )

# pobranie elementu z krotki:
print( tup1[2] )

# pobranie zakresu elementów:
print( tup1[2:5] )

# BŁĄD - nie można zmienić elementu krotki:
# tup1[3] = 4 # 'tuple' object does not support item assignment

# BŁĄD - nie można usunąć elementu krotki:
# del tup1[2] # 'tuple' object does not support item deletion

for x in tup1:
    print(x)

# najmniejsza wartość:
print( min(tup1) )

# największa wartość:
print( max(tup1) )

# konwersja listy na krotkę:
print( tuple( [3, 4, 5] ) )

# ćwiczenie:
tuple1 = (1, 2, 3, 4) + (5,) + tuple([6,7])
print( type(tuple1) )
print(tuple1) # (1, 2, 3, 4, 5, 6, 7)

print( 9 in tuple1 ) # False

