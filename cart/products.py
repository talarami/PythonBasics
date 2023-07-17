class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.name) + " " + str(self.price) # konwersja ceny na łańcuch znaków
    
class Phone(Product):
    def __init__(self, name, price, color):
        Product.__init__(self, name, price)
        self.color = color
    
    def __str__(self):
        return super().__str__() + " " + str(self.color) # super - uzyskanie dostępu do wszystkich elementów klasy nadrzędnej Product
         
 #phone1 = Phone("Phone X", 1000, "red")
 # print(phone1) # Phone X 1000 red

class TV(Product):
    def __init__(self, name, price, screenSize):
        super().__init__(name, price) # wywołujemy to czego wymaga nadrzędny konstruktor
        self.screenSize = screenSize
    def __str__(self):
         return super().__str__() + " " + str(self.screenSize)


# tv1 = TV("TV Y", 2000, 65)
# print(tv1) # TV Y 2000 65

