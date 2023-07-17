# Napisz program, który skorzysta z pętli while aby dodać wartości od 1 do 100. 
# Dodaj zmienną i równą 0, która będzie inkrementowana w pętli o 1. Kolejną zmienną będzie 
# sum z wartościąpoczątkową 0. W pętli while sprawdź czy i jest mniejsze równe 100. Wewnątrz
# pętli dodaj do sum wartość i, następnie zrób inkrementację i o jeden. Dodaj else po pętli
# while z tekstem w konsoli "Koniec pętli while". Zapisz podsumowanie: "Suma wartości" oraz wynik

i = 0
sum = 0

while i <= 100:
    sum += i
    i += 1
else:
    print("Koniec pętli while")

print("Suma wartości od 1 do 100:", sum)