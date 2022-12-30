numbers = [18, 14, 29, 22, 102, 178, 44, 12, 36, 99, 103]

for number in numbers:
    if number % 5 == 0:
        print(f"Found a number ! {number} is divisible by 5")
        break
    else:
        print(f"{number} is not divisible by 5")
else:
    print("No number div 5 was found...")