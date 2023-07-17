# zadanie: Stwórz zmienną wage poza funkcją o wartości 5000. Napisz funkcję raiseWage z dwoma
# parametrami liczbowymi: income oraz extra. W funkcji podnieś wartość income o 20%. Następnie
# zwrób sumę income i extra. Wywołaj funkcję raiseWage przekazując jako argument wage oraz 1000
# jako extra. Zachowaj zwracaną wartość w zmiennej updatedWage. Pokaż w konsoli wartości:
# wage i updatedWage, ponieważ przekazywane dane są niemutowalne to wage musi miec wartość 5k,
# a updatedWage odpowiednio wiekszą według implementacji funkcji.

def raiseWage(income, extra):
    income * 1.2
    return income + extra

wage = 5000
updatedWage = raiseWage(wage, 1000)

print("wage:", wage)
print("updatedWage:", updatedWage)