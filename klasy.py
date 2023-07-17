
# DEFINICJA KLASY VEHICLE:
# szablon:

class Vehicle:
    def __init__(self, brand, model, color, year): # zawsze musi być class i self na pierwszym miejscu
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.distanceTraveled = 1
        self.setMaxSpeed(150)
        self.displayInfo()
        
    def displayInfo(self):
        print(self.brand, self.model, self.color, self.year, self.distanceTraveled)

    def setMaxSpeed(self, newMaxSpeed):
        self.maxSpeed = newMaxSpeed

# wykorzystanie szablonu do stworzenia nowych aut:

corolla = Vehicle("Toyota", "Corolla", "sivler", "2016") # nie przekazujemy "self" w poszczególnych elementach, on występuje tylko w definicji konstruktora
corolla.distanceTraveled = 1000
corolla.setMaxSpeed(175)
corolla.displayInfo()

civic = Vehicle("Honda", "Civic", "black", 2018)
civic.setMaxSpeed(190)
civic.displayInfo()

# Definicja klasy wymaga słowa kluczowego class, po nim nazwę klasy z dużej litery oraz dwukropek.
# Następnie w klasie można zapisać zmienne oraz metody na których obiekt będzie operował.

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
print( person1.getFullName() )
person1.printData()
print( type(person1) ) # <class '__main__.Person'>

# Definicja klasyy to szablon na bazie którego powstaną obiekty w pamięci komputera. Są to plany 
# konstrukcyjne wykorzystywane przez Python do powołania instancji obiektu.

# W klasie może być zdefiniowana specjalna metoda tzw. konstruktor - _init_ będzie wywołana
# podczas tworzenia instacji obiektu. Konstruktor stosuje się do zainicjowania zmiennych wewnątrz
# klasy wartościami z argumentów przekazanych do konstruktora oraz innymi potrzebnymi operacjami.



