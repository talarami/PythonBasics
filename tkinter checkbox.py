import tkinter as tk

window = tk.Tk()

def valueChangeed():
    if cbValue.get() == 0:
        print("Checkbox is off")
    if cbValue.get() == 1:
        print("Checkbox is on")


cbValue = tk.IntVar(value=0)

c1 = tk.Checkbutton(window, text="Accept TOS", variable=cbValue, onvalue=1, offvalue=0, command=valueChangeed)
c1.grid(row=0)

window.mainloop()
