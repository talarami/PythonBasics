import tkinter as tk

window = tk.Tk()

def buttonClicked():
    print("Button clicked")
    quit()

button = tk.Button(
    window, 
    text="Quit app",
    bd=12, # grubość obramowania przycisku
    fg="yellow", # foreground kolor
    bg="blue",
    activeforeground="black",
    activebackground="silver",
    font="Times 20 bold",
    height=4,
    width=24,
    padx=8, # dopełnienie tekstu na osi
    pady=8,
    relief="flat", # styl przycisku
    command=buttonClicked
)

button.pack() # ułożenie przycisku ze względu na wartości
window.mainloop()



