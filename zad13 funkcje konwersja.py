# zadanie 
# Napisz program do konwersji czasu. Stwórz funkcję timeToSecons przyjmującą ilość godzin oraz minut i
# zwracającą ilość sekund. Jako parametry funkcji zapisz: hours, minutes. Skonwertuj 2h40min na sekundy
# i pokaż wynik. Stwórz funkcję timeToHours przyjmującą parametr minutes i zwracającą ilość godzin.
# Skonwertuj 150 min na godziny i pokaż wynik.

def timeToSecons(hours, minutes):
    return minutes * 60 + (hours * 60 * 60)

def timeToHours(minutes):
    return minutes / 60

print("czas na sekundy:", timeToSecons(2, 40))

print("ilość godzin:", timeToHours(150))
