# Dane wewnątrz obiektu możemy nie tylko odczytać ale również je zmienić wpisując po kropce (dot operator) 
# nazwę zmiennej/atrybutu i następnie po znaku równości nową wartość:

# person1.name = "Kasia" #nadpisanie
# person1.city = "waw" #dodanie nowej

# Jeżeli nie ma atrybutu to zostanie dodana nowa z odpowiednią wartością do obiektu, czyli dane mogą
# być dodawanie dynamicznie. Nie trzeba ich definiować w definicji klasy.

#ĆWICZENIE 1

class Person:
    def __init__(self, name, surname, country):
        self.name = name
        self.surname = surname
        self.country = country 

    def getFullName(self):
        return "Full name:" + self.name + " " + self.surname

    def printData(self):
        print(self.name, self. surname, self.country)

person1 = Person("Ola", "Kowalska", "Polska")
print( person1.name ) # uzyskanie dostępu do zmiennej/atrybutu name: Ola
person1.name = "Kasia" # nadpisanie
person1.city = "Waw" # dodanie nowej
print(person1.city) # Waw
person1.printData()

# ĆWICZENIE 2
import random

class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.schoolName = None
        self.fieldOfStudy = None

    def printInfo(self):
        print(self.name, self.surname, self.age, self.city, self.schoolName, self.fieldOfStudy)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.studentsList = []
        self.fieldsOfStudy = ["IT", "Math", "Robotics"]

    def addStudent(self, student):
        if isinstance(student1, Student): # zwróci True jeśli student1 jest instacją klasy drugiej Student
            self.studentsList.append(student)
            student.schoolName = self.name
            student.fieldOfStudy = random.choice(self.fieldsOfStudy)

    def printSchoolInfo(self):
        print("School name: ", self.name, "City: ", self.city)
        print("Students:")
        for el in self.studentsList:
            el.printInfo()


student1 = Student("Kasia", "Lis", 20, "Krk")
student1.schoolName = "Tech School 1"
student1.country = "Poland"
student1.printInfo() # Kasia Lis 20 Krk None None
print(student1.country)

student2 = Student("Adam", "Kowalski", 21, "Waw")

school = School("Tech School", "Waw")
school.addStudent(student1)
school.addStudent(student2)
print()
school.printSchoolInfo()

