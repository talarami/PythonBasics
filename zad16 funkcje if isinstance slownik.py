# zadanie: Napisz program z funkcją generateUser zwracającą słownik osoby. Stówrz funkcję 
# generateUser z parametrami: firstName, contactInfo. W ciele funkcji stówrz zmienną person
# która będzie słownikiem reprezentującym osobę. Parametr contactInfo będzie mógł przyjąć tekst
# lub liczbę. Sprawdź za pomocą isinstance jaki typ ma przekazany parametr contactInfo. Wywołaj
# funkcję z dwoma przypadkami: 
# imię Anna, contactInfo(string): anna@example.com
# imię Ada contactInfo(number): 123456789
# Pokaż zwrócone słowniki.

if isinstance ("text", str):
    print("text to łańcuch znaków")

if isinstance("text", int):
    print("text to łańcuch int") #nie wykona się

if isinstance("1245", int):
    print("wartość to int")


def generateUser(firstName, contactInfo):
    person = {
        "name": firstName,
        "email": None,
        "telephone": None
    }
