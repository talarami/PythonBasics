
list1 = [0, 1, 2, 3, 4, 5, 6]

# pobieranie elementu: 
print( list1[2] ) # 2

# pobieranie zakresu:
print( list1[2:4] ) # [2:3]

list2 = ["Ania", "Ola", "Rafał", "Adam"]

# zamiana elementu:
list2[2] = "Daniel" # "Rafał" na "Daniel"
print(list2) # w konsoli: ['Ania', 'Ola', 'Daniel', 'Adam']

# skasowanie elementu:
del list2[1] 
print(list2) # w konsoli: ['Ania', 'Daniel', 'Adam']

# długość listy:
print( len(list2) ) # 3

# największy element:
print( max([4, 8, 1]) ) # 8

# najmniejszy element:
print( min([4, 8, 1]) ) # 1

# zamiana krotki na listę:
tuple2 = ("Ola", "Adam")
newList = list(tuple2)
print(newList)

# łączenie:
print( [0,1] + [2, 3] ) # [0, 1, 2, 3]

# powtózenie:
print( [3, 2] * 2 ) # [3, 2, 3, 2]

print( 5 in [3, 4, 5] ) # True

print( 0 not in [3, 4, 5] ) # True

list3 = ["Ola", "Ania", "Adam"]
for x in list3:
    print(x)

# dodanie elementu:
list4 = ["Ania", "Ola"]
list4.append("Ola")
print(list4) # w konsoli: ['Ania', 'Ola', 'Ola']

# ilość powtórzeń:
print(list4.count("Ola")) # 2

# dodanie elementów do listy z innej sekwencji:
list4.extend(["Rafał", "Kasia"])
print(list4) # w konsoli: ['Ania', 'Ola', 'Ola', 'Rafał', 'Kasia']

# zwracanie najmniejszego indeksu wystąpienia wartości:
print(list4.index("Ola")) # 1

# umieszczenie elementu pod indeksem, przesuwa istniejący dalej:
list4.insert(0, "Kinga")
print(list4) # w konsoli: ['Kinga', 'Ania', 'Ola', 'Ola', 'Rafał', 'Kasia']

# odwrócenie kolejności:
list5 = [6, 0, 1, 2]
list5.reverse()
print(list5) # [2, 1, 0, 6]

# sortowanie:
list5.sort()
print(list5) # [0, 1, 2, 6]

# zwraca i zabiera ostatni element z listy:
print(list5.pop()) # 6
print(list5) # [0, 1, 2]

# Listy są mutowalne.
