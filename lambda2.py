# ćwiczenia

# sumowanie:


sum = lambda a,b: a + b # określamy ilość parametrów oraz nazwy, a później co ma się stać z tymi parametrami

print( sum(4,5) ) # 9
print( sum(14, 5) ) # 19

# dodanie funkcji, która zwróci wyrażenie lambda: 

def generateLambda(num):
    return lambda a: a * num # parametry, które będą przyjęte przez lambdę i co będzie zwrócone

doubler = generateLambda(2) # przekazujemy wartość 2
print( doubler(4)) # uzyskamy wartość 8, ponieważ wartość 2 jest przechowana wewnątrz tej wygenerowanej lambdy, 
                   # czyli wartość 2 będzie w num, będzie przechowana w lambdzie, zwrócona do doubler

# wykorzystanie lambda z funkcjami wyższego rzędu:

# funkcja map:

listData = [0,1,2,3]

result = list( map(lambda a: a * 3, listData) )
print(result) # w konsoli: [0, 3, 6, 9], czyli elementy pomnożone przez 3

# funkcja filter:

result = list( filter(lambda a: a > 1, listData)) 
print(result) # w konsoli: [2, 3], czyli elementy większe od 1

# funkcja reduce:

from functools import reduce

result = reduce( lambda x,y: x + " " + y, ("Ola", "Ania"))
print(result)

