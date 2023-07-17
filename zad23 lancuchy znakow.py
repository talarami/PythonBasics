
#konsultacja z Domisiem


# Zadanie string replace. Stwórz funkcję cleanText, która będzie czyścić przekazany tekst z określonych słów.
# Użyj funkcję replace do zamiany podanych słów na wykropkowane, które wielokrotnie może pojawić się
# w przekazanym łańcuchu. Zastąp następujące słowa kluczowe: JavaScript, java, php, html, css.
# Zwróć wyczyszczony tekst z funkcji cleanText. Wywołaj funkcję na następującym lub podobnym
# tekście:
# """Programowanie zacząłem z językiem php, następnie
#  poznałem: html i cdss, ale obecnie skupiam się na
#  JavaScript"""
# Wynik pokaż w konsoli.

def cleanText(text):
    text = text.replace("JavaScript", "*********")
    text = text.replace("java", "*" * 4)
    text = text.replace("php", "*" * 3)
    text = text.replace("html", "*" * 4)
    text = text.replace("css", "*" * 3) 
    return text

content = """Programowanie zaczęłem z językiem php, następnie
poznałem: html i css, ale obecnie skupiam się na JavaScript """

newContent = cleanText(content)
print(newContent)



              
    

