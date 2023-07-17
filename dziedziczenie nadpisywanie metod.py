# Dziedziczenie, tak jak nazwa wskazuje, jest mechanizmem, który pozwala 
# przekazać do klas sowa, orzeł, pingwin, informację, że cześć cech oraz metod jest 
# zdefiniowana w innej klasie, a one same, są potomkami tej klasy:

# klasa ptak, ma kolor, szybkość, wielkość, lata, wydaje odgłosy

# klasa sowa, potomek klasy ptak, dodatkowo czuwa w nocy

# klasa orzeł, potomek klasy ptak, dodatkowo poluje

# kasa pingwin, potomek klasy ptak, jednak nie lata, ale umie się ślizgać

# Co jak widzimy znacząco może nam uprościć definicje klas sowa, orzeł, pingwin i pozwolić 
# na skupieniu się, tylko na tych aspektach, które faktycznie te klasy charakteryzują.
# Można przypisać nową wartość do odziedziczonych atrybutów.

class ptak:
    def __init__ (self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc
        
    def lec(self):
        print ("Tu", self.gatunek, "  Startuje, i zaraz osiagne predkosc", self.szybkosc)
        
    def wydajOdgłos(self):
        pass # pusty konstruktor
    
class orzel (ptak):
    def poluj(self):
            print ("Tu", self.gatunek, "  Rozpoczalem polowanie")
        
class pingwin (ptak):
    def slizgaj(self):
        print ("Tu", self.gatunek, "  Rozpoczalem slizg")
        
    def lec(self):
        print ("Tu", self.gatunek, "  Przykro mi, ale nie latam")


# ćwiczenie 2:

class Vehicle:
    def __init__(self):
        self.brand = "unknown"
        self.name = "unknown"
        self.topSpeed = 100
        self.numWheels = 4

    def printVehicleInfo(self):
        print(self.brand, self.name, self.topSpeed) # unknown unknown 100

vehicle1 = Vehicle()
vehicle1.printVehicleInfo()

class Car(Vehicle):
    def printCarInfo(self): # można nadpisać odziedziczone atrybuty
        self.brand = "Ford"
        self.name = "Mustang"
        print("Car brand: ", self.brand)
        print("Car name: ", self.name)

car1 = Car()
car1.printCarInfo() 
