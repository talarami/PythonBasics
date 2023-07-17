
# Poniżej jest definicja klasy Car na której podstawie powstaną obiekty. Klasa to taki szablon co powołany obiekt ma zawierać, np. zmienne oraz metody.

class Car: # specjalna metoda inicjująca obiekt, jest wywołany podczas utworzenia instancji obiektu
    def __init__(self, brand, model, year):
        self.carName = brand + " " + model # self to pierwszy parametr zawsze mający obiekt na rzecz którego wywołana jest metoda
        self.productionDate = year 


# Metoda printInfo otrzymuje tylko jeden obowiązkowy parametr self czyli obiekt na którym jest wywołana metoda:

def printInfo(self):
    print( self.carName + " " + str(self.productionDate ))

# Klasa Car używana jest jako szablon do powołania dowolnej ilości obiektów na jej podstawie, poniżej dwa obiekty klasy Car:

mustang = Car("Ford", "Mustang", 1970)
mustang.printInfo()

viper = Car("Dodge", "Viper", 1997)
viper.printInfo()




