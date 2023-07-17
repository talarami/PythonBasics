# Wyrażenia lambda są to jednolinijkowe anonimowe funkcje bez nazwy. Tworzone za pomoć słowa
# kluczowego lambda po który następuje lista parametrów. Po dwukropku znajduje się właściwy kod funkcji.
# Funkcję lambda można też przypisaćdo zmiennej i wywołać jak zwykłą funkcję.

# Poniższa funkcja lambda przyjmuje dwa argumenty a oraz b i zwraca ich sumę, return nie jest
# potrzebne, wynik wyrażenia jest automatycznie zwracamy z lambda.

sum = lambda a,b: a + b

print( sum(10,5)) #w konsoli: 15

print(sum(4,3)) #w konsoli: 7

# Wyrażenie lambda może być również zwrócone przez zwykłą funkcję, dzięki czemu można ją wywołać w razie potrszeb.

# zwrócona jest funkcja lambda, która zapamięta wartość n:

def genFunc(n):
    return lambda a: a * n

doubler = genFunc(2) # w doubler jest lambda z n o wartości 2

print(doubler(5)) #10
print (doubler(7)) #14

tripler = genFunc(3)

print(tripler(2)) #6
print(tripler(3)) #9

# Wyrażenia lambda z map() przydają się najbardziej w funkcjach takich,
# które jako argument przyjmują inne funkcje lub zwracają funkcję.

# Funkcja r = map(func, seq) przyjmuje funkcję którą wywoła na wszystkich elementach seq
# po czym zwróci sekwencję zmotyfikowanych przez func elementów w postaci Iteratora,
# więc można skonwertować wynik na listę poprzez list().

listData = [1, 2, 3, 4, 5]

result = map(lambda x: x*2, listData)
print(list(result)) # [2, 4, 6, 8, 10]

print(list(map(lambda x: x *3, [1, 2, 3, 4]))) # [3, 6, 9, 12]

# Funkcja filer przyjmuje wyrażenia lambda, które jeśli zwróci true sprawi, że dany element listy 
# znajdzie sięw wynikowej sekwencji.

listData = ["Ola", "Włodzimierz", "Kasia", "Izydor"]

# filtruje imiona, wybiera te, które mają mniej niż 6 liter:
result = filter(lambda x : len(x) <= 5, listData)

print(list(result)) # w konsoli: ['Ola', 'Kasia']

# Funkcja reduce redukuje sekwencję do pojedynczej wartości:

from functools import reduce # import funkcji reduce

tab = [2, 1, 3, 4, 5]

numSum = reduce((lambda x, y: x+y), [1, 2, 3, 4, 5])

print ("Suma liczb:", numSum)




