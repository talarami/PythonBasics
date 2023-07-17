#zadanie: sprawdzenie wymagań dla potencjalnego kandydata na programistę. Dodaj zmienną experience
# z wartością 3, kolejną languages z listą elementów: "python", "typescript", "javascript", "java".
# Dodaj zmienną conctractType o wartości "employment". Wykorzystaj instrukcję if z operatorem and
# do sprawdzenia czy doświadczenie kandydata to dwa lub więcej lat oraz czy zna język python i java.
# Jeśli powyższe warunki są spełnione zrób kolejny if i sprawdź czy typ kontraktu to "b2b" lub
# "employment". W przypadku gdy warunki if nie są spełnione pokaż w konsoli po else odpowiednią
# informację.

experience = 3
languages = ["python", "typescript", "javascript", "java"] 
conctractType = "employment"

if experience >=2 and "python" in languages and "java" in languages:
    print("Kandydat spełnia wymagania")

if conctractType == "employment" or "b2b":
    print("Kandydat zostaje przyjęty")
