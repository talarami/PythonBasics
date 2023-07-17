# Zadanie:
# Stwórz klasę PhoneSimCard reprezentującą kartę sim telefonu z kontaktami. Klasa PhoneSimCard tworzy zmienną klasy phoneContacts jako listę 
# w konstruktorze. Dodaj metodę addPhoneContact przyjmującą oprócz self również parametry contactName i phoneNumber. Sprawdź z funkcją
# isinstance czy przekazane dane są prawidłowe czyli str i int. Stówrz słownik z contactName i phoneNumber i dodaj go do listy
# kontaktów obiektu powstałego na bazie klasy. Napisz metodę displayContacts, która w pętli pokaże kolejne kontakty w terminalu. 
# Stwórz instancję klasy PhoneSimCard. Dodaj poniższe kontakty: 
# - "Ela", 987654321
# - "Tomasz", 12345678
# - 200,12345678
# - "Marta", "numer"
# Część danych jest nieprawidłowa więc nie powinny być dodane przesz addPhoneContact. Wyświetl kontakty z displayContacts().

class PhoneSimCard:                                                                          
    def __init__(self):
        self.phoneContacts = []
    
    def addPhoneContact(self, contactName, phoneNumber):
        if not isinstance(contactName, str): return
        if not isinstance(phoneNumber, int): return
    
        contact = {
            "contactName" : contactName,
           "phoneNumber" : phoneNumber
        }
        self.phoneContacts.append(contact)

    def displayContacts(self):
        for contact in self.phoneContacts:
            print(contact["contactName"], " ", contact["phoneNumber"])

phoneSim = PhoneSimCard()
phoneSim.addPhoneContact("Ela", 987654321)
phoneSim.addPhoneContact("Tomasz", 123456789)
phoneSim.addPhoneContact(200, 9876632423)
phoneSim.addPhoneContact("MArta", "numer")

phoneSim.displayContacts()
    

