# SCOPE
string = "Hello"

def showInfo():
    print(3, string)

def printData():
    string = "Test"
    print(2, string)
    showInfo()

printData()

# SCOPE ĆWICZENIA

number = 12

def test1():
    print(number) #ponieważ nie mamy zdefiniowanej lokalnej zmiennej o nazwie
                  #number wewnątrz tej funkcji to odwołujemy się do zmiennej globalnej
                  #w konsoli: 12

test1() #w konsoli: 12

def test2():
    number = 100 #przysłonienie zmiennej globalnej w kontekście wywoływanej funkcji
    print(number) #w konsoli: 100
    if 1 == 1:
        print(number)
        if 2 == 1:
            number = 50
            print(number) #w konsoli: 50, modyfikacja wartości lokalnej zmiennej
    print(number) #w konsoli: 50, ponieważ wartość lokalnej zmiennej została zmodyfikowana
                  #wewnątrz instrukcji if, wewnątrz funkcji test2

test2() #w konsoli: 100
print(number) #w konsoli: 12

# modyfikacja wartości zmiennej globalnej:

print("\n test3") 
def test3():
    global number
    number = 5
    print("test3", number) #w konsoli: 5
    if 1 == 1:
        number  = 6 #odwołanie do zmiennej globalnej wewnątrz funkcji
        print("test3", number) #w konsoli: 6

test3()
print("global number after test3():", number) #w konsoli: global number after test3(): 6

# przesłonięcie globalnej zmiennej number również wystąpi jeżeli będziemy mieli o takiej samej
# nazwie argument wewnątrz funkcji:

print("\ntest4")

number = 10
def test4(number):
    print("test4 param:", number) #w konsoli: 33
    number = 20
    print("test4 after change:", number) #w konsoli: 20

test4(33)
print("global number after test4():", number) #w konsoli: 10

# dwie funkcje, jedna wywołuje drugą:

print("\ntest5")    

number = 10
def foo():
    print("foo() number:", number) #w konsoli: 10

def bar():
    number = 9 #utworzenie lokalnej zmiennej
    print("bar() number: ", number) #w konsoli: 9
    foo() #w konsoli: 9

foo()
bar()
print("global number after foo() bar():", number)

# zdefiniowanie zagnieżdżonych informacji:

print("n\ check1 &check2")

number = 10

def check1():
    number = 12
    print("bar() number: ", number) #12 (gdyby w funkcji nie było zdefiniowanego number to python przyjąłby wartość globalną number czyli 10)
    def check2():
        print("foo() number:", number) #12
    check2() 

check1()
print("global number after check1():", number) #10

# utworzenie globalnej zmiennej przez instrukcję if (if/while/try/except nie definiują zasięgu, więc nie można utworzyć lokalnej zmiennej):

print("\nif test")

if 1 == 1:
    data = 100 #utworzy zmienną globalną

print("data in global scope:", data) #w konsoli: 100

if 2 == 1:
    nextData = 15

# print("nextData in global scope:", nextData) #bład, if nie jest spełnione, więc się nie wykona













