# Hermetyzacja gettery i settery - dekorator properties pozwala na wywołanie metody ustawiających 
# i pobierających dane z prywatnych zmiennych czyli gettery i settery.

class Vehicle:
    def __init__(self):
        self.__gears = 5 # na prywatny użytek klasy Vehicle jest __gears

@property # getter, pobiera wartość
def gears(self):
    if(self.__gears > 0):
        return self.__gears
    else:
        return -1
    
vehicle1 = Vehicle()
vehicle1.gears = 7 
vehicle1.printGears()


@gears.setter # setter, ustawia wartość; setter nie pozwala na ustawienie wartości ujemnej
def gears(self, gears):
    if(gears > 0): self.__gears = gears

def printGears(self):
    print("Gears: ", self.  gears)



vehicle1 = Vehicle()
vehicle1.gears = 7 # odwołanie do zmiennej gears z zewnątrz obiektu, przypisanie wartości do gears np 7 
                   # oznacza że Python automatycznie wywoła metodę setter
vehicle1.printGears()

vehicle1.gears = -2
vehicle1.printGears()