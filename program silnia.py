
# Program, który oblicza silnię z liczby. Silnia działa w ten sposób, że w praktyce będziemy rekurencyjnie wywoływali tę samą funkcję.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Podaj liczbę całkowitą:")) # konwersja na liczbę całkowitą

result = factorial(n)

print("Silnia z " + str(n) + " równa się:" + str(result)) # str(result) - konwersja na łańcuch znaków z result
