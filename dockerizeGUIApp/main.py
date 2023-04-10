import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()


def show_message():
    showinfo("Some Title", "Hello Paul !")


btn = tk.Button(root, text="Click Me!", command=show_message)
btn.pack()

root.mainloop()
