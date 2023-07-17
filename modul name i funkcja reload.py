# Moduł __name__ wskazuje nazwę modułu lub __main__ (główny plik naszego programu).

# Moduł reload() - każdy import wykonuje kod z zaimportowanego pliku:

# PLIK 1 - otherTest:

import random

print( "random from otherTest.py " + random.randint(0,100) )

# Istnieje możliwość ponownego importu modułu i wykonanie jego kodu dzięki modułowi importlib i metody reload():

# PLIK 2 - otherProg:

import otherTest
import importlib

print("OtherProg test")

# reload importuje wcześniej zaimportowany moduł:

importlib.reload(otherTest)
importlib.reload(otherTest)


