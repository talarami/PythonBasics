
import time

ticks = time.time()
print(ticks) # np. 1687340355.39074 - ilość sekund od 01.01.1970

# Przystępną funkcją zwracającą aktualny czas jest time.localtime(), która zwraca zarówno datę jak i czas w formie przystępnej krtki (tzw named tuple).

timeData = time.localtime()
print(timeData)
print(timeData.tm_year) # 2023
print(timeData.tm_mon) # 6
print(timeData.tm_mday) # 21
print(timeData.tm_hour) # 11
print(timeData.tm_min) # 52
print(timeData.tm_sec) # 14
print(timeData.tm_wday) # dzień tygodnia od 0 do 6: 2 (środa)
print(timeData.tm_yday) # dzień roku od 1 do 365: 172
print(timeData.tm_isdst) # 1

# Do funkcji time.localtime() można przekazać timestamp czyli ilość sekund od 01.01.1970
ticks = time.time()
print(ticks) # np. 1687340355.39074 

# Odjęcie jednej doby od aktualnego timestamp:
timeData = time.localtime( ticks - (24 * 60 * 60) )
print(timeData)

# Funkcja time.asctime() formatuje w wygodny sposób datę i czas dostarczoną przez time.localtime().

# 1687343541.5985544

result = time.asctime( time.localtime(time.time()) )
print("Wynik:", result) # Wynik: Wed Jun 21 12:32:21 2023

# Funkcja time.strftime() formatuje datę i czas na string według podanego wzoru, korzysta z oznaczeń,
# które będą zastąpione konkretnymi wartościami w tekście: %Y - rok, %m - miesiąc, %d - dzień,
# %H - godzina, %M - minuty, %S - sekundy.

timeData = time.localtime() # aktualny czas
timeStr = time.strftime("%m/%d/%Y %H:%M:%S", timeData)
print(timeStr) # 06/21/2023 12:35:46

# Funkcja time.strptime() parsuje łańcuch znaków i tworzy z niego krotkę z datą i czasem.
import time
timeStr = "08 March, 2025"
timeData = time.strptime(timeStr, "%d %B, %Y") # dzień miesiąca, nazwa miesiąca, rok
print(timeData) # time.struct_time(tm_year=2025, tm_mon=3, tm_mday=8, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=67, tm_isdst=-1)

# Funkcja time.sleep() usypia główny wątek programu na określoną ilość sekund.
i = 0
while i < 10:
    time.sleep(1) # usypia wątek programu na sekundę
    print( time.asctime( time.localtime() ) )
    i += 1 

# Pomiar czasu wykonywania programu:
import time

# pomiar czasu wykonywania kodu:

tStart = time.perf_counter() 

time.sleep(0.1)

tEnd = time.perf_counter()

# measure wall time
interval = tEnd - tStart
print("Elapsed time:", interval, "second") # Elapsed time: 0.10069210000801831 second

import datetime

datetimeObj = datetime.datetime(2023, 6, 21) # utworzenie obiektu datetime z daty
datetime = datetime.datetime(2025, 5, 30, 23, 59, 0)
datetimeObj = datetime.now() # aktualny czas i data
print("date(): ", datetimeObj.date() ) # 2023-06-21
print("time(): ", datetimeObj.time() ) # 13:15:47.501965
print("timestamp(): ", datetimeObj.timestamp() ) # 1687346147.501965 # ilość sekund od 1970 r.
print("weekday(): ", datetimeObj.weekday() ) # 2
print("today(): ", datetimeObj.today() ) # 2023-06-21 13:15:47.505726
print("year(): ", datetimeObj.year ) # 2023
print("hour(): ", datetimeObj.hour ) # 13
print("minute(): ", datetimeObj.minute ) # 15
print("second(): ", datetimeObj.second ) # 47
print("microsecond(): ", datetimeObj.microsecond ) # 501965
print("format(): ", datetimeObj.strftime( "%m / %d / %Y %H : %M : %S")) #  06 / 21 / 2023 13 : 15 : 47

# ćwiczenie:

import time
import datetime

timeStr = "12:23:45 21.06.2023"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y")
print(timeData)

# uśpienie wątku na pół sekundy w każdej iteracji, następnie wyświetlenie aktualnego czasu
i = 0
while i < 12:
    time.sleep(0.000005)
    print(time.asctime(time.localtime()))
    i += 1

# policzenie ile wykonuje się kod:

tStart = time.perf_counter()
time.sleep(1.2)
tEnd = time.perf_counter()
print("Code took:", (tEnd - tStart), "seconds")

