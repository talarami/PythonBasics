# ĆWICZENIE 1

class Magazine:
    def __init__(self, author, title = "unknown", isbn = "unknown", year = "unknown"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def displayData(self):
        print(self.title, self.author, self.isbn, self.year)


mag1 = Magazine(title = "Cars of the Year", author = "Redactor", year = 2001)
mag1.displayData()

mag2 = Magazine(title = "Trucks of the Year", author = "Redactor", isbn = 1434, year = 2001)
mag2.displayData()

# ĆWICZENIE 2

class Computer:
    def __init__(self, cpu, ram = 8192, gpu = "NVIDIA", price = 2000):
        self.setCpu(cpu)
        self.setRam(ram)
        self.gpu = gpu
        self.price = price

    def setCpu(self, cpu):
        if cpu.lower() == "amd" or cpu.lower() == "intel" or cpu.lower() == "arm":
            self.cpu = cpu
        else:
            self.cpu = "unkown"

    def setRam(self, ram):
        if type(ram) == int and ram >= 4096:
            self.ram = ram
        else:
            self.ram = 8192
    
    def displayInfo(self):
        print(self.cpu, self.ram, self.gpu, self.price)

computer1 = Computer("Intel", 16000)
computer1.displayInfo()

computer2 = Computer("AMD", 32000, 8000)
computer2.displayInfo()