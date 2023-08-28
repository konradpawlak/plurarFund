import random

m = int(input("haw many rolls do you want to do?\n"))

for i in range(0, m+1):
    j = random.randint(1, 7)
    print(f"you have rolld: {j}")