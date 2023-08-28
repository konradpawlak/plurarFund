import random

roll = random.randint(1, 6)

guess = int(input('Pick a number and try to geuss the dice roll:\n'))

if guess == roll:
    print(f"its {roll} ,you have guessed RIGHT!")
else:
    print(f"nope, it was: {roll}, better try next time bro!")