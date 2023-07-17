# Obsługa wyjątków - programy w Python mogą reagować na różne nieprzewidziane błędy,
# dzięki czemu mimo problemów mogą zareagować i kontynuować pracę. 

# Poniżej wyjątek przerywa działanie programu:
data = ["Ania", "Ola", "Kasia"]

print(data[2])
print(data[5]) # program się zakończy

# Poniżej wyjątek prawidłowo jest obsłużony:
import sys
data = ["Ania", "Ola", "Kasia"]

print(data[2])

try:
    print(data[5])
except:
    print("Error: ", sys.exc_info()[0]) # program się nie zakończy, będzie możliwość zareagowania na błąd

print(data[0])

# Dodatkowo można wskazać konkretny wyjątek, który ma być obsłużony np. IOError dla błędów podczas pracy z plikami.

# W programie otwarto plik w tej samej ścieżce co skrypt, jest obsługa błędu IOError jeśli zaistnieje.
# Jeśli jest wszystko w porządku jak nie będzie błędu po else zostanie zamknięty dostęp do pliku:

import os # sometimes script runs in different folder from where it is located
script_dir = os.path.dirname(__file__)
print(script_dir) # absolute path to run script

fh = None
try:
    fh = open(script_dir + "/test.txt", "w")
    fh.write("content")
except IOError:
    print("IOError occured")
else: 
    print("closing file")
    fh.close()


# Wywoływanie wyjątku.
# Aby zgłosić błąd w programie Python wystarczy użyć raise. Oczywiście błąd ten można przechwycić
# za pomocą try i except.

num = 10

try:
    if num > 0:
        raise Exception("Exception info")
except:
    print("Exception handled!")
    

