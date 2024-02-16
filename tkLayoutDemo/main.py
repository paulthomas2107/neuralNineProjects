import tkinter as tk

root = tk.Tk()
# root.geometry('300x170')

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

label1 = tk.Label(frame1, text='Label 1:')
entry1 = tk.Entry(frame1)
label2 = tk.Label(frame1, text='Label 2:')
entry2 = tk.Entry(frame1)
button1 = tk.Button(frame2, text='Button 1')
button2 = tk.Button(frame2, text='Button 2')

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack()
button2.pack()
frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.LEFT)


""" Pack
label1.pack(padx=5, pady=5, side=tk.LEFT)
entry1.pack(padx=5, pady=5, side=tk.LEFT)
label2.pack(padx=5, pady=5, side=tk.LEFT)
entry2.pack(padx=5, pady=5, side=tk.LEFT)
button1.pack(padx=5, pady=5)
button2.pack(padx=5, pady=5)
"""

""" Grid 
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
button1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
button2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
"""

""" Place
label1.place(x=10, y=10)
entry1.place(x=70, y=10)
label2.place(x=10, y=50)
entry2.place(x=70, y=50)
"""

""" Pack #2 
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack(expand=True, fill=tk.X)
button2.pack(expand=True, fill=tk.X)
"""


root.mainloop()