# 1. ask what emopte to add
# 2. ask for definition to it
# 3. open file
# 4. wrtie new emote and definition to the file
def find_meme():
    look_up = input("What meme would you like to check definition of?\n")

    found = False
    try:
        with open('D:\python nauka\memki.txt') as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('Yooo someone stole our file bro. its not there??!1')
        return
        
    if not found:
        print('There is no definition for this meme')

def add_emote():
    emote = input('What emote you want to add?\n')
    definition = input('Follow up with definition:\n')

    with open('D:\python nauka\memki.txt', 'a') as file:
        file.write(emote + ' - ' + definition + '\n')

def main():
    # ask if search or to add
    choice = input('Yo bro, you want oto find(F) or add(A) an emote??')
    if choice == 'F' or 'f':
        find_meme()
    elif choice == 'A' or 'a':
        add_emote()

main()