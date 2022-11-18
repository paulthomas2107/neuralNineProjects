from tabulate import tabulate
import numpy as np
import pandas as pd


table_data = [
    ['Name', 'Age', 'Job'],
    ['Mike', 22, 'Programmer'],
    ['John ', 32, 'Teacher'],
    ['Keith', 28, 'Dentist'],
    ['Paul', 38, 'Footballer'],
    ['Julie', 35, 'Developer']
]

print(tabulate(table_data, headers="firstrow", tablefmt="psql"))
print(tabulate(table_data, headers="firstrow", tablefmt="plain"))
print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

print(tabulate(table_data, headers="firstrow", tablefmt="html"))
with open('mytable.html', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="html"))
with open('mytable.tex', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="latex"))


data = {
    'Name': ['Mike', 'John', 'Keith', 'Paul', 'Julie'],
    'Age': [22, 32, 28, 38, 35],
    'Job': ['Programmer', 'Teacher', 'Dentist', 'Footballer', 'Developer']
}

print(tabulate(data, headers='keys', tablefmt="fancy_grid", showindex="always"))


columns = ['COL1', 'COL2', 'COL3']
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(tabulate(array, headers=columns, tablefmt="fancy_grid", showindex="always"))


df = pd.DataFrame(data)
print(df)
print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex="always"))
