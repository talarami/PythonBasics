# ćwiczenie

class Employee:
    numEmployees = 0
    employeesList = []

    def __init__(self, name):
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