import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total
player1 = input("Whats the name of player1?: \n")
player2 = input("Whats the name of player2?: \n")

# roll1 = random.randint(1, 6) + random.randint(1, 6) # same as randint 2-12
# roll2 = random.randint(1, 6) + random.randint(1, 6) # mozna tak albo zrobic funkcje jak wyzej

roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled:', roll1)
print(player2, 'rolled:', roll2)

if roll1 > roll2:
    print(player1, 'has won!')
elif roll1 < roll2:
    print(player2, 'has won!')
else:
    print('No winners! Its a draw!')