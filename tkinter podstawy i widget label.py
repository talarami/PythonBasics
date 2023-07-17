
# Tkinter - biblioteka Pythona umożliwiająca tworzenie aplikacji z interfejsem użytkownika (GUI).
# Utworzenie okna wymaga powołanie instancji klasy TK czyli Tkinter.
# Okno pozwala na zmianę np. tytułu na belce aplikaccji.
# Etykietę tworzy się na podstawie klasy Label.
# mainloop() to nieskończona pętla czekająca na zdarzenie od użytkownika aby je przeprocesować 
# tak długo jak okno nie zostało zamknięte.

import tkinter as tk
# window is instance of tkinter class:
window = tk.Tk() # uchwyt do okna
window.title("Application") # app title

# make label:
label1 = tk.Label(
    text="Ja Talarek",
    foreground="blue",
    background="pink"
)
# add label to window:
label1.pack() 

label2 = tk.Label(
    text="Ty Domiś",
    foreground="deep pink", # text color
    background="light green" # background color
)
label2.pack()

label3 = tk.Label(
    text="A to wszystko vis a vis",
    foreground="purple",
    background="yellow"
)
label3.pack()

window.mainloop() 

# Label - etykieta wyświetla tekst w oknie
# Widget Label wyświetla tekst lub obrazek w określonym oknie (master) oraz akceptuje wiele potencjalnych argumentów.
# Argument anchor przyjmuje wartość: NW, N, NE, W, CENTER, E, SW, S, SE.


label1 = tk.Label ( master = window,
    text = "Hello World \n Hello Again \n A to wszystko vis a vis",
    foreground="white", # text color
    background="green",
    width=20, # grubość linii
    height=3,
    cursor = "dot", # arrow, dot
    anchor= tk.E, # east - to the right
    font = "Helvetica 16 bold italic underline",
    padx = 5, # extra space to the left and right
    pady = 5, # extra space to the top and down
)  
label1.pack()
window.mainloop()


