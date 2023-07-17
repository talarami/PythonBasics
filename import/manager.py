# Rozszerzenie klasy Employee i następnie zaimportowanie manager do main.py.

from typing import Any
from user import User, Employee # dostęp do User i Employee bezpośrednio, nie trzeba stosować user.employee

class Manager(Employee):
    def __init__(self, name):
        Employee.__init__(self, name)

    def __str__(self):
        return "Manager: " + str(self.name)
    
# Manager został stworzony. Teraz nastąpi jego import do pliku main.py.