# Wyświetlenie elementów listy od końca z pętlą while. Stwórz listę elementów: Jan, Tomek,
# Beata, Alicja. Zapisz zmienną i, od której w każdej iteracji pętli odejmiesz 1; to indeks
# elemetu w liście. Wpisz wartość początkową zmiennnej i jako ostatni indeks listy, czyli
# element "Alicja". W pętli while sprawdź czy i jest większe lub równe zero. Pobierz imię 
# z listy, używając numeru indeksu w i, i wyświetl je w konsoli. Zmień wartość zmiennej i.

elementList = ["Jan", "Tomek", "Beata", "Alicja"]
i = len(elementList) - 1 #długość listy - 1 (bo lista zawsze liczy o 1 za dużo)

while i >= 0:
    person = elementList[i]
    print(person)
    i -= 1