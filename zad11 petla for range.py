#zadanie: Stwórz zmienną total, która będzie miała ustawioną wartość 0 przed każdą pętlą. Zrób
# pętlę for z wartościami od 0 do 200 z range, zsumuj liczby i wyświetl rezultat w konsoli. Zrób
# pętlę for z range z liczbami od 50 do 100, dodaj je i wyświetl wynik. Zrób kolejną pętlę z range
# od 0 do 300 z krokiem co 3, dodaj liczby i wyświetl wynik.

total = 0
for n in range(201):
   total += n

print("suma od 0 do 200:", total)