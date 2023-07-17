import sys # pokaże rodzaj błędu


data = ["Ola", "Ania", "Adam", "Kasia"]

print(data[0]) # Ola

index = 10
try:
    print(data[index]) # błąd: indexError: list index out of range, trzeba dodać try
    print(data[index - 1])
    # raise Exception("some error") # zgłaszanie błędu
except IndexError:
    print("Error Index Error", sys.exc_info()[0]) # Error Index Error <class 'IndexError'>
except InterruptedError:
    print("Error Interrupted Error", sys.exc_info()[0])
except:
    print("Error", sys.exc_info()[0]) 
else:
    print("No error") # w konsoli "No error", jeśli zmienimy index np na 2

print(data[3]) # Kasia

