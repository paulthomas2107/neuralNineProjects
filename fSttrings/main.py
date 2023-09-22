import locale
import babel.numbers
import decimal
import datetime

name = 'Mike'
age = 79

print(name + ' is ' + str(age) + ' years old')
print(f'{name} is {age} years old')

weight = 80.6526
print(f'{name} is {age} years old and weighs {weight:.2f} kg')

win_rate = 0.67
print(f'Win Rate is {win_rate:.2%}')

# Hex x
print(f'{name} is {age: x}({age: X}) years old')

# Octal o
print(f'{name} is {age:o} years old')

# Binary
print(f'{name} is {age:b} years old')

# Scientific e
print(f'{name} is {age:e} years old')

# Separators
net_worth = 123456789.12
# Locales
print(f'{name}: net worth ${net_worth:,}')
locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')
print(f'{name}: net worth £{net_worth:n}')
# Currency
locale.currency(12345678, grouping=True)
print(f'{name}: net worth £{net_worth:n}')

# Babel
print(f'{name}: net worth {babel.numbers.format_currency( decimal.Decimal(net_worth), "EUR")}')

# Leading Zero
day = 7
month = 6
year = 2023
print(f'Date: {day:02}/{month:02}/{year}')

# More
print(f'{12345678:_b}')

# Width formatting
sentence = 'Each column has a width of ten'
table = ''
for word in sentence.split(' '):
    table += f'{word:<10}'
print(table)

words = ['Paul', 'Rory', 'Caitlin']
print(f'1. {words[0]:.<20} $100')
print(f'2. {words[1]:#<20} $200')
print(f'3. {words[2]:_<20} $300')

# Dates
current = datetime.datetime.now()
print(f'{current}')
print(f'{current:%y}')
print(f'{current:%m}')
print(f'{current:%d}')
print(f'{current:%H}')
print(f'{current:%m}')
print(f'{current:%S}')
print(f'{current:%j}')
print(f'{current:%Y-%m-%d %H:%M:%S}')