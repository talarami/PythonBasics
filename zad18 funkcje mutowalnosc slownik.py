# zadanie: Przekazywanie mutowalnych danych do funkcji jak słownik, zadanie. Utwórz słownik opisujący
# pracownika i zapisz go w zmiennej worker. Do elementów słownika dodaj: name, email, rank(stopień 
# wpisz programmer), salary(8000). Napisz funkcję elevateToManager która przyjmuje parametr
# o nazwie person gdzie przekazany będzie słownik. Wewnątrz funkcji zmień wartości elementow
# przekazanego słownika person, podnieś pensję o 50%, zmień rank na manager. Dodatkowo sprawdź
# czy przekazany pracownik jest już managerem, w takim wypadku podaj w konsoli, że ta oosba jest
# już managerem i wyjdź z funkcji z return. Wywołaj funkcję elevateToManager i przekaż utworzony
# na początku słownik.

worker = {
    "name": "Ania",
    "email" : "anna@example.com",
    "rank" : "programmer",
    "salary" : 8000
}

def elevateToManager(person):
    if person["rank"] == "manager":
        print("Osoba", person["name"], "jest już managerem")
        return
    
    person["rank"] = "manager"
    person["salary"] *= 1.5

elevateToManager(worker)
print(worker)
