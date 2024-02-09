import re
import tkinter as tk


def find_matches():
    pass


def check_match():
    pass


root = tk.Tk()
root.title('RegEx Checker')

regex_label = tk.Label(root, text='Enter Regex:')
regex_label.grid(row=0, column=0, padx=5, pady=5)

regex_entry = tk.Entry(root, width=50)
regex_entry.grid(row=0, column=1, padx=5, pady=5)

text_label = tk.Label(root, text='Enter Text:')
text_label.grid(row=1, column=0, padx=5, pady=5)

text_entry = tk.Text(root, width=50, height=10)
text_entry.grid(row=1, column=1, padx=5, pady=5)

find_button = tk.Button(root, text='Find Matches', command=find_matches)
find_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='we')

check_button = tk.Button(root, text='`Check Match', command=check_match)
check_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='we')

result_label = tk.Label(root, text='', fg='green')
result_label.grid(row=4, column=0, columnspan=2,  padx=5, pady=5)

root.mainloop()