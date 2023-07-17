
data = { "name" : "Kasia", "city" : "Waw" }

# pobieranie elementu:
print( data["name"] ) # Kasia

# modyfikacja elementu:
data["name"] = "Ola"

# tworzenie kolejnego elementu słownika:
emailKey = "email"
data[emailKey] = "ola@example.com"
print(data) # {'name': 'Ola', 'city': 'Waw', 'email': 'ola@example.com'}

# skasowanie elementu:
del data["city"]
print(data) # {'name': 'Ola', 'email': 'ola@example.com'}

# skasowanie wszystkich elementów:
data.clear()
print(data) # {}

# długość słownika:
data = { "name" : "Ola", "city" : "Waw"}
print( len(data) ) # 2 

# kopia słownika:
data = { "name" : "Kasia", "city" : "Waw"}
copy = data.copy() # tworzy płytką kopię słownika
print(copy)

# tworzenie słownika z podanymi kluczami, wartości jako None
print(data.fromkeys( ("name", "email", "country") )) # {'name': None, 'email': None, 'country': None}

# zwraca istniejącą wartość klucza lub drugi argument:
print( data.get("postal code", "DEFAULT") ) # nie ma "postal code", więc zwraca DEFAULT

# sprawdzenie czy klucz jest w słowniku
print( "name" in data ) # True

# zwraca listę kluczy:
print( data.keys() ) # dict_keys(['name', 'city'])

# zwraca listę wartości:
print( data.values() ) # dict_values(['Kasia', 'Waw'])

