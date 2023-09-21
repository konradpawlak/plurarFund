# program that opens and reads files according to users chosen memes
# IMOPORTANT! ALWAYS CLOSE OPENED FILE AFTER WORKING ON IT

# file = open('D:\python nauka\memki.txt')

# with open('D:\python nauka\memki.txt') as file:
    # do file operations here, it will close itself afterwars

look_up = input("What meme would you like to check definition of?\n")

found = False
with open('D:\python nauka\memki.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
if not found:
    print('There is no definition for this meme')