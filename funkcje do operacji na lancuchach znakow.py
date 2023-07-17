
print ( "Hello" + "World!") # konkatenacja Hello World!

# powtórzenie HelloHello:
print( "Hello" * 2)

string = "Hello"
print( string[1] ) # e
print( string[1:3] ) # wyświetla zakres od 1 do 3 (pierwsza litera to 0), w konsoli: el
print("o" in string) # True
print ("x" not in string) # True

# tekst w wielu liniach:
multiLine = """ line 1
line 2
""" 
# utworzenie łańcucha znaków w dużą literą na początku:
print( "some text". capitalize() ) # w konsoli: Some text

# zlicza ilość "ok":
print ( "ok ok ok".count("ok") ) # w konsoli: 3

# wycentrowanie tekstu do 10 znaków z * :
print( "test".center(10, "*") ) # w konsoli: ***test***

print("Hello world".endswith("world")) # True
print("Hello world".startswith("Hel")) # True

# wyszukiwanie łańcucha, -1 jeśli nie ma lub pozycja w str:
print( "Ala ma kota".find("ma") ) # w konsoli: 4, czyli jest pod 4 znakiem
print( "Ala ma kota". find("test") ) # w konsoli: -1, bo nie ma

# rfind() wyszukuje od końca:
print("Ola ma psa, Ola ma kota".rfind("Ola")) # w konsoli: 12, bo jest na 12 znaku od końca

# likwidacja białych znaków od lewej strony:
print( "\n \t Test ".lstrip() ) # "Test "

# likwidacja białych znaków od prawej strony:
print ( " Test \n \t ".rstrip() ) # " Test"

# likwidacja białych znaków po obu stronach:
print( " \n \t Test \n \t ".strip() ) # "Tekst"

# zamienienie wystąpienia jakiegoś łańcucha znaków na inny:
print( "Ola ma kota, Ola ma psa".replace("Ola", "Ania") ) # w konsoli: Ania ma kota, Ania ma psa

# sprawdzenie czy podany łańcuch znaków jest liczbą całkowitą:
print( "123456".isalnum() ) # True

# sprawdzenie czy podany łańcuch znaków ma tylko liczby alfabetu:
print( "123456".isalnum() ) # False
print( "Test".isalnum() ) # True
print( "Test 2".isalnum() ) # False

# sprawdzenie czy podany łańcuch znaków zawiera tylko małe litery:
print ( "test".islower() ) # True

# sprawdzenie czy podany łańcuch znaków zawiera tylko białe znaki:
print ( " \t ".isspace() ) # True

# sprawdzenie czy podany łańcuch znaków zawiera tylko wielkie litery:
print ( "HELLO".isupper() ) # True

# łączenie łańcuchów w jeden string z separatorem:
print( "-".join( ["Ola", "Ania"] ) ) # Ola-Ania

# długość łańcucha znaków:
print( len("str length") )

# zmniejszenie liter w łańcuchu znaków:
print( "HELLO WORLD".lower() ) # hello world

# zwiększenie liter w łańcuchu znaków:
print( "hello world".upper() ) # HELLO WORLD

# odwrócenie wielkości liter w łańcuchu znaków:
print( "HELLO world".swapcase() ) # hello WORLD

# formatowanie danych:
print( "My name is {myName}, I'm from {country}".format(myName = "Kuba", country = "Poland")) # w konsoli: My name is Kuba, I'm from Poland
print( "My name is {myName}, my postal code is {code}".format(myName = "Kuba", code = 11789)) # w konsoli: My name is Kuba, my postal code is 11789
print( "My name is {0}, my postal code is {1}".format("Kuba", 11789)) # w konsoli: My name is Kuba, my postal code is 11789
print( "My name is {}, my postal code is {}".format("Kuba", 11789)) # w konsoli: My name is Kuba, my postal code is 11789



