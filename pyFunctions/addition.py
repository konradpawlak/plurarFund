# def
def addition(a, b):
    return a + b

# main
# num1 = float(input('please insert 1st digit/number: \n'))
# num2 = float(input('please insert 2nd digit/number: \n'))
# result = addition(num1, num2)
# print('Your result is: ', result)

# tak jak wyzej jest spoko
# ale warto to wrzucic
# w jedna duza funcje main

def main():
 num1 = float(input('please insert 1st digit/number: \n'))
 num2 = float(input('please insert 2nd digit/number: \n'))
 result = addition(num1, num2)
 print('Your result is: ', result)

main()