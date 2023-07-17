#zadanie: Napisz program decydujący czy wyjść czy zostać w domu zależnie od pogody. Dodaj zmienne:
# raining = False, haveUmbrella = False, temperatur = 14. Sprawdź czy temperature jest powyżej 
# lub równa 40 lub poniżej lub równa 0. W takim wypadku wyświetl "Zostań w domu". Jeśli powyższy
# warune nie jest spełniony w elif sprawdź kolejny czy temperatura jest powyżej 0 oraz poniżej
# 10 stopni oraz ma parasolkę i pada, w takim wypadku wyświetl "Możesz wyjść z parasolką". Gdy
# żadne z powyższych nie jest spełnione sprawdź w kolejnym elif czy nie pada i temperatura jest
#powyżej lub równa 10 to wyświetl: "Możesz wyjść bez parasolki". Na koniec dodaj domyślną opcję
# z informacją "Zostań w domu".

raining = False
haveUmbrella = False
temperature = 14

if temperature >=40 or temperature <=0:
    print("Zostań w domu")
elif temperature > 0 and temperature < 10 and haveUmbrella == True and raining:
    print("Możesz wyjść z parasolką")
elif raining == False and temperature >=10:
    print("Możesz wyjść bez parasolki")
else:
    print("Zostań w domu")
