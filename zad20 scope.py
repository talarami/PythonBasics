# zadanie
# Stwórz globalną zmienną employees, która jest pustą listą. Napisz funkcję addEmployee która przyjmuje email i salary, 
# wewnątrz stwórz słownik z tymi samymi parametrami. Następnie dodaj go do globalnej listy employees
# stosując funkcję append. Wywołaj funkcję addEmployee dla trzech dowolnych pracowników o pensjach: 6000, 8000 i 10000, wpisz 
# dowolne maile. Dodaj funkcję increaseSalary z dwoma argumentami: employees i pctIncrease. Jako pierwszy
# argument będzie przekazywana lista pracowników, a do drugiego wartość podwyżki. Przejdź po wszystkich
# pracownikach i zwiększ pensję pracowników o przekazaną wartość procentową pctIncrease. Zwiększ pensje
# pracowników z funkcją increaseSalary o 20%, wyśweitl liste w terminalu.

employees = []

def addEmployee (email, salary):
    e = {
        "email": email,
        "salary": salary
    }
    employees.append(e)
    
addEmployee("ania@test.com", 6000)
addEmployee("ada@test.com", 8000)
addEmployee("ola@test.com", 10000)

#pctIncrease np 20
def increaseSalary(employees, pctIncrease):
    pctIncrease *= 0.01

    for e in employees: #lokalne employees nadpisze to globalne
        e["salary"] *= 1 + pctIncrease

increaseSalary(employees, 20)
print(employees) # w konsoli: [{'email': 'ania@test.com', 'salary': 7200.0}, {'email': 'ada@test.com', 'salary': 9600.0}, {'email': 'ola@test.com', 'salary': 12000.0}]


