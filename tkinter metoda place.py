# Metoda place() - umieszzcza elementy dokładnie we wskazanym miejscu

# x, y- położenie na osi x oraz y w pikselach, oś x zaczyna się wartością0 w lewym górnym rogu, dodatnie
# wartości x do prawej strony ekranu, dodatnie wartości y w dół ekranu

# width, height - wielkość widgetu w pikselach

import tkinter as tk

window = tk.Tk()

l1 = tk.Label(window, text="Text 1", bg="white")
l1.place(x=10, y=10)

l2 = tk.Label(window, text="Label 2", bg="yellow")
l2.place(x=100, y=10, height=50, width=80)

entry = tk.Entry(window)
entry.place(x=50, y=100)

window.mainloop()