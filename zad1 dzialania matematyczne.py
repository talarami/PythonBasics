# Oblicz zwrot inwestycji po roku, zapisz poniższe zmienne
# initialInvestment - 6000
# interestRate - 0.1 czyli 10%
# inflation - 0.12 czyli 12 %
# Oblicz zwrot z inwestycji oraz o ile spadła wartość kapitału z uwagi na inflację.
# Dodaj do kapitału zwrot z inwestycji oraz odejmij utracony kapitał z uwagi na inflację.

initialInvestment = 6000
interestRate = 0.1
inflation = 0.12

InvestmentReturn = initialInvestment * interestRate
print("Zwrot z inwesytcji:", InvestmentReturn) #zwrot o 600


InflationLow = initialInvestment * inflation
print("Spadek wartości ze względu na inflację:", InflationLow) #spadek o 720


print("Wartość końcowa:", initialInvestment + InvestmentReturn - InflationLow)