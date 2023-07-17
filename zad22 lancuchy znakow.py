
# do konsultacji z Domisiem



# String i find(). Napisz funkcję validateEmail sprawdzającą w podstawowy sposób czy email jest prawidłowy. Wykorzystaj find() do wyszukania fargmentów 
# tekstu w email: 
# - sprawdź czy istnieje w przekazanym do funkcji emailu znak @, zapisz index w monkeyIndex
# - posiadając pozycję @ sprawdź czy istnieje znak kropki po małpie, zapisz pozycję kropki w dotIndex
# - jeżeli wszystkie powyższe warunki są spełnione zwróć True, w innym wypadku False
# Wywołaj funkcję z następującymi mailami, pokaż co zwraca w konsoli funkcja:
# - asia@example.com
# - karol@domena
# - user.com

def validateEmail(email):
    monkeyIndex = email.find("@")
    print("malpa jest na pozycji ", monkeyIndex)
    if monkeyIndex < 0: return False

    dotIndex = email.find(".")
    print("kropka jest na pozycji ", dotIndex)
    if dotIndex == -1: return False
    if dotIndex < monkeyIndex: return False
    
    return True

email2 = "kar.ol@domena"
print(email2, validateEmail(email2))


"""
email1 = "asia@example.com"
print(email1, validateEmail(email1))

email2 = "karol@domena"
print(email2, validateEmail(email2))



email3 = "user.com"
print(email3, validateEmail(email3))
"""


