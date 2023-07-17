# Hermetyzacja - cała idea polega na ukrywaniu wybranych parametrów oraz metod klasy, tak aby nie były dostępne z zewnątrz. 
# A jedynie na użytek wewnętrzny klasy. Metody i zmienne będą prywatne jeśli mają przedrostek z 
# podwójnym podkreśleniem, są tylko dostępne w obiekcie na bazie tej klasy.

class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __getGearsInfoStr(self):
        return "gears number: " + str( self.__gears )
    
# Klasa car rozszerza klasę Vehicle i próbuje uzyskać dostęp do prywatnej metody,
# kończy się to błędem interpretera Pythona. Car nie ma dostępu do _getGearsIntoStr():

class Car(Vehicle): 
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
    
    def printInfo(self):
        print(self.__getGearsInfoStr()) 

car1 = Car("Dodge")
