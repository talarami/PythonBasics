# zadanie: Napisz program z dwoma funkcjami do konwersji temperatury. Stwórz funkcję cToF, któa
# skonwertuje stopnie Celsjusza na Fahrenheita z wzoru: celsius * 9/5 + 32. Stwórz funkcję
# fToC, która konwertuje stopnie Fahrenheita na Celsjusza z wzoru: celsius = (fahreheit-32) * 5/9.
# Dodatkowo w konsoli pokaż wynil. Znak stopni: \xB0. Skonwertuj 20 stopni na Fahrenheita.
# Skonwertuj 86 stopni na Celsjusza.

def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "stopni Celsjusza to", fahrenheit, "stopni Fahrenheita")
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(fahrenheit, "stopni Fahrenheita to", celsius, "\xB0 Celsjusza")
    return celsius

convertedFahrenheit = cToF(20)
convertedCelsius = fToC(86)
