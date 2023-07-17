import tkinter as tk

window = tk.Tk()

scrollbar = tk.Scrollbar(window)
textBox = tk.Text(window, height=6, width=100, padx=5, pady=5, font="Times 18 bold")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox.pack(side=tk.LEFT, fill=tk.Y)
scrollbar.config(command=textBox.yview) # żeby scrollbar był w stanie kontrolować treść w textBox
textBox.config(yscrollcommand= scrollbar.set)

textBox.insert(tk.END, "Hello World \n Hello Again");

window.mainloop()
