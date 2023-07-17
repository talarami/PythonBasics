from products import *

class Cart:
    def __init__(self):
        self.__productsList = []
        self.__cartValue = 0

    def addProduct(self, product):
        #if isinstance(product, Phone) or isinstance(product, TV):
        if isinstance(product, Product):
            if product not in self.__productsList:
                self.__productsList.append(product)
                self.calculateCart()

    def calculateCart(self):
        self.__cartValue = 0
        for el in self.__productsList:
            self.__cartValue += el.price

    def __str__(self):
        strData = "\nCart info, products list:"
        for el in self.__productsList:
            strData += "\n - " + str(el.name) + " " + str(el.price)
        strData += "\n cart value: " + str(self.__cartValue)
        return strData
    
phone1 = Phone("Phone X", 1000, "red")
tv1 = TV("TV Y", 2000, 65)

cart = Cart()
cart.addProduct(phone1)
cart.addProduct(tv1)
cart.addProduct(tv1)
cart.addProduct("test") 
print(cart)