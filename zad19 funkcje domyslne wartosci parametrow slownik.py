# zadanie: Domyślne wartości parametrów. Napisz funkcję z parametrami: email, country z domyślną
# wartości "USA", company z domyślną wartością "Sample Corp". Zwróć z funkcji słownik z 
# elementami jak parametry. Przetestuj funkcję z jednym elementem john@example.com oraz drugi
# przypadek z john@example.com będącym z UK.

def createPerson(email="ania@mailxxxx.com", country="USA", company="Sample Corp"):
    return {
        "email": email,
        "country": country,
        "company": company
    }

print(createPerson("john@example.com"))
print(createPerson(country="UK", email = "john@example.com"))