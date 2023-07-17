# Zmienną statyczną tworzymy wewnątrz klasy, poza konstruktorem i metodą. Ciekawą właściwością takiej statycznej
# zmiennej jest fakty, że jest tylko jedną i jedyną dla wszystkich instancji obiektu na bazie danej klasy.

# W przykładzie zmiennąstatyczną jest numEmployees zdefiniowana na poziomie klasy. Dostęp do niej
# uzyskuje się poprzez nazwę klasy i nazwę zmiennej statycznej. 

class Employee:
    numEmployees = 0 # statyczna, wspólna zmienna dla wszystkich obiektów na bazie klasy employee

    def __init__(self, name):
        self.name = name
        print("self.name: ", self.name)

        Employee.numEmployees += 1 # zwiększenie wartości wspólnej statycznej zmiennej
        print("Employee.numEmployees", Employee.numEmployees)

employee1 = Employee("Ola")
employee2 = Employee("Asia")
employee3 = Employee("Kasia")
print("number of employees: ", Employee.numEmployees)
