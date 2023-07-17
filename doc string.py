# Doc string to łańcuch znaków w pierwszej linijce definicji funkcji, metody czy klasy.
# Może być pobrany za pomocą nazwy klasy oraz atrybutu _doc_.
# Takie łańcuchy stanowią opis działania danej funkcjonalności większej części kodu np
# klasy, modułu itd. Nie należy mylić tych informacji z komentarzami, które opisują konkretny kod, np jak działa.

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.printDocString()

    def printDocString(self):
        print( Person.__doc__)


person1 = Person("Ola", "Kowalska")

# Jest wiele zmiennych oraz metod pozwalających na dostęp do informacji o klasie/obiekcie oraz atrybutach,
# np. _name_, _module_.

class Person:
    def __init__(self, name, surname):
        print( Person.__name__ ) # nazwa klasy
        self.name = name

        print( Person.__module__ ) # nazwa modułu w którym zdefiniowana jest klasa, _main_ w trybie interaktywnym
        print( hasattr(self, "city") ) # hasattr sprawdza czy w danym obiekcie istnieje jakiś atrybut; False
        print( hasattr(self, "name") ) # True
        print( getattr(self, "name") ) # getattr pobiera wartość atrybutu; Ola
        setattr(self, "country", "Poland") # ustawienie nowego atrybutu
        print(self.country) # Poland
        delattr(self, "country") # skasowanie atrybutu

person1 = Person("Ola","Kowalska")

# ćwiczenie 

class Employee: 
    "Employee class descibing company employee"
    #static variables for all objects based on Employee
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
        "Constructor for Employee"
        """
        line 1
        line 2
        """
        self.name = name

        Employee.numEmployees += 1
        print(self.name, "numEmployees: ", Employee.numEmployees)

        Employee.employeesList.append(self)

    def printAllEmployees(self):
        for el in Employee.employeesList:
            print(el.name)


employee1 = Employee("Ola")
employee2 = Employee("Kasia")
employee3 = Employee("Adam")
employee4 = Employee("Karol")

print("Employee.numEmployees: ", Employee.numEmployees)
print()

employee1.printAllEmployees()

print(Employee.__doc__) # Employee class descibing company employee
print(Employee.__name__) # Employee
print(Employee.__module__) # __main__

print("name attr in Employee: ", hasattr(employee1, "name")) # True
print("name attr in Employee: ", hasattr(employee1, "city")) # False
employee1.city = "Krk"
print("name attr in Employee: ", hasattr(employee1, "city")) # True

setattr(employee1, "name", "Kasia")
print("employee1.name: ", getattr(employee1, "name"))