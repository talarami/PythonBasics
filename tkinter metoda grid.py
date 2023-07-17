# Metoda grid() - umieszcza elementy w dwuwymiarowej tabeli

# column - kolumna, domyślnie 0, czyli lewa kolumna
# row - wiersz, domyślnie 0, czyli na górze
# padx, pady - dopełnienie osi x i y na około widgeta
# ipadx, ipady- dopełnienie wewnątrz
# columnspan - ile kolumn zajmuje widget, domyślnie 1
# rowspan - ile wierszy zajmuje widget, domyślnie 1

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Name: ")
label1.grid(row=0, column=0, padx=2, pady=2)

label2 = tk.Label(window, text="Surname: ")
label1.grid(row=1, column=0, padx=2, pady=2)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1, padx=2, pady=2)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1, padx=2, pady=2)

window.mainloop()