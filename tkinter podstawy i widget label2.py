
import tkinter as tk
import os # potrzebne do importu obrazka z komputera

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

window = tk.Tk()
window.title("Application")
logo = tk.PhotoImage(file="img.png")

label1 = tk.Label(window, 
        text="Hello World",
        foreground="white",
        background="black",
        width = 20,
        height = 3, # ilość linii
        cursor= "dot", # co będzie pokazane jak użytkownik najedzie kursorem na label
        font="Times 18 bold italic underline",
        anchor= tk.W,
        padx= 5,
        pady=5
)
label1.pack() # żeby etykieta (label) wyświetliła się wewnątrz aplikacji

label2 = tk.Label(window, text="Hello Again")
label2.pack() 

label3 = tk.Label(window,  # label z obrazkiem
                  text="Hello World",
                  image=logo,
                  width=200,
                  height=200,
                  foreground="red",
                  compound=tk.CENTER)
label3.pack() 

label3.config(text="Hello World \n Hello Again") # zmiana jednej z wartości label


window.mainloop() # działanie w tle, gwarancja że aplikacja się nagle nie zamknie

