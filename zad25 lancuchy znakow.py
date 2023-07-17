

# String - zadanie. Napisz funkcję getEmailParts przyjmującą parametr email. Wykorzystaj pobieranie fragmentów tekstu
# w python aby rozłożyć email na części i zapisz je w zmiennych:
# - user - od początku emaila do ostatniego znaku przed @
# - domainName - tekst za @ i przed kropką
# domainExt - tekst za ostatnią kropką do końca
# Zwróć słownik z funkcji z elementami jak powyższe zmienne. Pamiętaj aby użyć find aby określić pozycję indeksu
# małpy w email, jeśli go nie ma zwróć None z funkcji, podobnie z kropką.
# Przetestuj funkcję na emailu:
# ola@domena.com


def getEmailParts(email):
    monkeyInd = email.find("@")
    if monkeyInd == -1: return None

    dotInd = email.rfind(".")
    if dotInd == -1: return None

    user = email[0 : monkeyInd],
    domainName = email[monkeyInd+1 : dotInd],
    domainExt = email[dotInd+1 : len(email)]

    return {
        "user": user,
        "domainName": domainName,
        "domainExt": domainExt
    }

print(getEmailParts("ola@domena.com"))


    
