# Stwórz zmienną accountBalance z wartością początkową 1200. Dodaj wartość nowej pensji 8000. 
# Odejmij 2500 kosztow za mieszkanie. Błąd banku pomnożył Twoje saldo czterokrotnie.
# ODejmij 5000 na samochód. Bank zorientował się, że powstał błąd i cofa ostatnie transakcje.
# Dodaj do salda 5000, podziel je przez 4 i dopiero teraz odejmij 5000. Pokaż saldo końcowe.

accountBalance = 1200
accountBalance += 8000
print(accountBalance)

accountBalance -= 2500
print(accountBalance)

accountBalance *= 4
print(accountBalance)

accountBalance -= 5000
print(accountBalance)

accountBalance += 5000
print(accountBalance)

accountBalance //= 4
print(accountBalance) 

accountBalance -= 5000
print(accountBalance)