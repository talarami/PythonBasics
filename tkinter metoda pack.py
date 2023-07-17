# Metoda pack() - umożliwia rozmieszczenie elementow w blokach wewnątrz okna.

# expand - jeśli true widget rozszerza się na dostępną przestrzeń
# fill - czy widget wypełni dodatkową przestrzeń albo zajmie minimalną przestrzeń - None - domyślnie,
# X - wypełni się horyzontalnie, Y - wypełni się wertykalnie, Both - obie 

import tkinter as tk
window = tk.Tk()

label1 = tk.Label(window, text="Information text #1")
label1.pack(side = tk.TOP, expand = True)

label2 = tk.Label(window, text="Next information text #2")
label1.pack(side = tk.TOP, expand = True)

label3 = tk.Label(window, text="Bottom information text #2")
label1.pack(side = tk.BOTTOM, expand = True)

button1 = tk.Button(window, text="Opt 1", fg="red")
button1.pack(side = tk.LEFT)

button2 = tk.Button(window, text="Opt 2", fg="blue")
button2.pack(side = tk.RIGHT)

window.mainloop()