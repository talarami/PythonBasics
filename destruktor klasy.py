# Destruktor to specjalna metoda wywoływana kiedy niszczony jest opeikt za pomocą operatora del. Zanim obiekt
# będzie skasowany z pamięci destruktor daje nam szansę na jeszcze jakieś ostatnie operacje np.
# zamknięcie dostępu do plików itp.

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print("Object created: "+self.getFullName())

    def getFullName(self):
        return self.name + " " + self.surname
    
    def _del_(self): # destruktor
        print("Zniszczenie obiektu: " + self.getFullName())

person1 = Person("Ola", "Kowalska")
print( person1.name ) # uzyskanie dostępu do zmiennej/atrybutu name: Ola
print( person1.surname )
print("Full name: ", person1.getFullName() )
del person1 # zniszczenie obiektu i wywołanie destruktora
