# ćwiczenie

class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __getGearsInfoStr(self):
        return "gears number " + str(self.__gears)
    
    def printInfo(self):
        print(self.brand, self.name, self.__getGearsInfoStr())


vehicle1 = Vehicle("Dodge", "Charger")
# print(vehicle1.__gears) #błąd
# vehicle1.__getGearsInfoStr() #błąd
vehicle1.printInfo() # Dodge Charger gears number 5

print( vehicle1._Vehicle__gears ) # dostanie się do wartości wewnątrz: 5

print(vehicle1._Vehicle__getGearsInfoStr()) # dostanie się do wartości wewnątrz: gears number 5


class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
        print(self.__gears)

# car1 = Car("Ford", "Mustang") # błąd: 'Car' object has no attribute '_Car__gears'

