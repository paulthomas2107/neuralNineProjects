import random

colors = ['Red', 'Green', 'Yellow', 'Blue', 'Purple', 'Orange']
code_length = 4
max_attempts = 10

code = random.choices(colors, k=code_length)

attempts = 0

print("Welcome To The NeuralNine Mastermind Game")
print(f"Available colors: {','.join(colors)}")
print(f"Code length: {code_length}, Max Attempts: {max_attempts}")

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ").strip().split()
    if len(guess) != code_length or not all(color in colors for color in guess):
        print("Invalid guess. Make sure you have FOUR colors")
        continue

    correct_position = sum(g == c for g, c in zip(guess, code))
    correct_color = sum(min(guess.count(c), code.count(c)) for c in set(code))
    correct_color -= correct_position

    print(f"{correct_position} colors placed correctly !")
    print(f"{correct_color} correct colors placed in wrong positions !")

    if correct_position == code_length:
        print("Congratulations ! You Won !")
        exit()

    attempts += 1

print("You have lost !")
print("The correct code was ", code)