# ABC - abstract base class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod # dekorator
    def speak(self):
        pass # brak implementacji


class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Miau")

dog = Dog()
dog.speak()

cat = Cat()
cat.speak