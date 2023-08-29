expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum1 = 0
sum2 = sum(expenses)

for x in expenses:
    sum1 = sum1 + x
print(f'You spent: {sum1} pln')
print(f'You spent: $', sum1, sep = '')
print('You spent: $', sum2, sep = '')

# instead of asking for input 7 times like this:
# 
# expenses = []
# expenses.append(float(input("Enter an expense:\n")))
# expenses.append(float(input("Enter an expense:\n")))
# ...
# you can loop it
# 
# range(7) ========> (0,1....6)
# range(0, 7, 1) ==> (0,1....6)
# range(2, 14, 2) => (2,4...12)
secpense = []
n = int(input("how many items add to the list and sum it up?\n"))
for i in range(n):
    secpense.append(float(input(f"Enter an expense no {i+1}:\n")))

total = sum(secpense)
print(f'You spent: {total} plnów mordo')