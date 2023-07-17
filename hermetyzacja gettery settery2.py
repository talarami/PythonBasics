class Vehicle:
    def __init__(self):
        pass # pusty konstruktor

    @property #getter
    def gears(self): #nazwa metody gettera
        print("getter:", self.__gears) # getter: 8
        if(self.__gears > 0):
            return self.__gears
        else:
            return -1
        
    @gears.setter
    def gears(self, newGears): # "newGears" jako argument ustanawiający nową wartość
        print("newGears:", newGears) # newGears: 8
        if(newGears > 0): self.__gears = newGears


vehicle1 = Vehicle()
vehicle1.gears = 8
print(vehicle1.gears) # 8