# Im więcej kodu pisze y tym bardziej rośnie potrzeba modularyzacji i organizacji naszego programu, aby
# łatwiej było kontrolować i odnaleźć się w kodzie źródłowym. Przykładowo każda z klas może być w
# oddzielnym pliku, a dopiero główny plik importujący poszczególne klasy wykorzysta je w faktycznym
# programie. Dodatkowo pliki z klasami mogą być użyte w innych programach co oszczędza nam czas.

# Instrukcja import importuje jako moduł dowolny kod z innego pliku. Powinno się unikać spacji.

# Instrukcja import pozwala na import wielu modułów po przecinku za jednym razem. Moduł jest
# importowany tylko raz niezależnie ile razy była wywołana instrukcja import.

# Instrukcja from import pozwala na import specyficznych elementów do aktualnej przestrzeni nazw
# naszego programu. Przestrzeń nazw (tzw. namespaces) to w praktyce słownik z unikalnymi nazwami
# zmiennych jako klucze, a wartości słownika to wartości zmiennych.

# np. from user import User, Employee
# gdzie user to nazwa pliku a User i Employee to nazwy klas w tym pliku

# Instrukcja from user import* zaimportowałaby wszystkie elementy z danego modułu.
