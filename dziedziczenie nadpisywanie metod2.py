
# ćwiczenie:

class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.topSpeed = 10
        self.numWheels = 4

    def printVehicleInfo(self):
        print("printVehicleInfo: ", self.brand, self.name, self.topSpeed, self.numWheels)

vehicle1 = Vehicle("Vehicle", "basic")
vehicle1.printVehicleInfo()

class Car(Vehicle): # piszemy po której klasie dziedziczymy
    def printCarInfo(self):
        print("printCarInfo: ", self.brand, self.name, self.topSpeed, self.numWheels) # printCarInfo: Ford Mustang 10 4
    
    def printVehicleInfo(self):
        print("Car.printVehicleInfo: ", self.brand, self.name, self.topSpeed, self.numWheels)

    def printNumWheels(self):
        print("Vehicle.numWheels: ", self.numWheels)

car1 = Car("Ford", "Mustang")
car1.printCarInfo()
car1.printVehicleInfo() # printVehicleInfo: Ford Mustang 10 4
car1.printNumWheels()

class SuperCar(Car):
    def reachSpeed300(self):
        self.topSpeed = 301
        print("Super car reached 300!")

superCar1 = SuperCar("Ford", "GT")
superCar1.reachSpeed300() # Super car reached 300!
superCar1.printVehicleInfo() # Car.printVehicleInfo: Ford GT 301 4
superCar1.printNumWheels() # Vehicle.numWheels: 4

