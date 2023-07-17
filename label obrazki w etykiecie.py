# Label - obrazki w etykiecie
# Etykieta może być wzbogacona o obrazek, w takim wypadku argument width i height wskazuje na ilość pikseli.

import tkinter as tk
import os

window = tk.Tk()
scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
logo = tk.PhotoImage(file="img.png")

# tekst
label1 = tk.Label(
    master=window,
    text="Hello World \n Hello Again",
    foreground="black",
    width=10,
    height=3,
    cursor= "dot",
    font="Helvetica 16 bold italic underline"
)
label1.pack(side="left")

#obrazek
label2 = tk.Label(
    master=window,
    image=logo,
    width=200,
    height=200
)
label2.pack(side="right") # z prawej strony 
window.mainloop()

# Aby połączyć tekst i logo wymagany jest argument compound = tk.CENTER.

window = tk.Tk()
scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
logo = tk.PhotoImage(file="img.png")

label1 = tk.Label(
    master=window,
    text="Hello World",
    compound= tk.CENTER,
    font="Helvetica 16 bold italic underline",
    image=logo
)

label1.pack(side="left")
#config() dinamically changes content:
label1.config(text="Hello World \n Hello Again")
window.mainloop()

