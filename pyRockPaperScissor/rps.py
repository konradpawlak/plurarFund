from random import choice

choose = ['rock', 'paper', 'scissors']

computer_choice = choice(choose)
print('computer choose: ', computer_choice)
# = random.choice(list) ==> works as well
user_choice = input('Do you want rock, paper or scissors?\n')

if computer_choice == user_choice:
    print("its a TIE!")
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("you WIN!")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("you WIN!")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("you WIN!")
else:
    print("you have LOST!")