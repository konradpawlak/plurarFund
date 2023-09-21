# prgram that needs exceptions
# a divider

def remainder_division(a,b):
    if b == 0:
        raise ZeroDivisionError
    elif b < 0:
        raise Exception('Divisor cannot be negative')
    
    result = a//b
    remainder = a%b
    print(a, '/', b, 'id', result, 'remainder', remainder)

# main program

remainder_division(10,3)
remainder_division(10,0)
remainder_division(10,(-1))

# still something to fix here