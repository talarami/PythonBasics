
# Przykład ma dwie klasy, tylko bazowa - Person posiada konstruktor. Po uruchomieniu programu i
# utworzeniu obiektu na bazie klasy Employee okazuje się, ze konstruktor klasy bazowej Person
# został wywołany automatycznie:

class Person:
    def __init__(self):    
        print("Person constructor")

class Employee(Person):  # klasa Employee nie posiada konstruktora
    def printInfo(self):
        print("Employee info")

employee1 = Employee()

# Przekazanie argumentu do konstruktora potwierdza, że poniższe utworzenie egzemplarza Employee 
# w tym przypadku uruchomi od razu konstruktor Person, bo nie ma konstruktora Emoployee:

class Person:
    def __init__(self, name): 
        self.name = name      
        print("Person constructor", self.name)

class Employee(Person): 
    def printInfo(self):
        print("Employee info")

employee1 = Employee("Ola")

# Utworzenie egzamplarza instancji Employee wywołuje konstruktor Employee, gdyż
# istnieje on w definicji tej klasy:

class Person:
    def __init__(self, name): 
        self.name = name      
        print("Person constructor", self.name)

class Employee(Person): 
    def printInfo(self, name):
        self.name = name
        print("Employee constructor", self.name)
    
    def printInfo(self):
        print("Employee info")

employee1 = Employee("Ola")