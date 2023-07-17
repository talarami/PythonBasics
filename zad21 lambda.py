# Zadanie: Stwórz listę names z wartościami: Ola, Ania, Kasia. Z pomocą mapy i lambdy dodaj do każdego
# imienia tekst "Kowalska". Wyświetl nową listę w konsoli. Przefiltruj nową listę ze względu
# na długość tekstu, zachowaj w nowej liście tylko te które mają więcej niż 12 znaków. Pokaż 
# przefiltrowaną listę w konsoli.

nameList = ["Ola", "Ania", "Kasia"]

result = list( map(lambda a: a + " " + "Kowalska", nameList) )
print(result)

result = filter(lambda x : len(x) > 12, result)
print(list(result))