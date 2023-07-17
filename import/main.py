# Importowanie pliku user jako moduł.

import user
from manager import Manager # import manager

print("main:", user.user1) # User: Ola
                           # main: User: Ola

# tworzenie nowego pracownika:

employee1 = user.Employee("Adam")
print("main:", employee1) # main: Employee: Adam

# importowanie tylko poszczególnych elementów za pomocą from import.

manager1 = Manager("Kasia")
print("main: ", manager1) # main:  Manager: Kasia
