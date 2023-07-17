import tkinter as tk

window = tk.Tk()

def buttonClicked():
    print("Button clicked")

def buttonChangeColor():
    button.configure(bg="red", fg="yellow")

button = tk.Button(
    window, 
    text="Change color",
    bd=12, # grubość obramowania przycisku
    fg="yellow", # foreground kolor
    bg="blue",
    font="Times 20 bold",
    height=4,
    width=24,
    padx=8, # dopełnienie tekstu na osi
    pady=8,
    relief="flat", # styl przycisku
    command=buttonChangeColor
)

button.pack() # ułożenie przycisku ze względu na wartości


window.mainloop()