
words = input("Podaj listę słów oddzielonych przecinkami:").split(",") # split rozdziela elementy ze względu na przecinek

words = [ word.strip() for word in words ] # usunięcie białych znaków między słowami podanymi przez użytkownika

dictionary = {}

for word in words:
    firstLetter = word[0].lower()
    if firstLetter in dictionary:
        dictionary[firstLetter].append(word)
    else:
        dictionary[firstLetter] = [word]

for key in sorted(dictionary.keys()):
    print(key + " : " + str(dictionary[key]) )
    