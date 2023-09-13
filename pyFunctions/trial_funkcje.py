
# defs
# local
def greeting(name):
    print('Hello,',name,'-san')
# global
def farawell():
    print('Sayonara,', surname)
# local 2
def witaj(nick):
    print('Yooo,',nick,'-bro')

# Main program
name1 = input('Whats ur name?\n')
greeting(name1)

# print(name) <- name not defined, cant print. its local var for function

surname = input('Whats ur surname was?\n') # global
farawell()


# back to local scope
name2 = 'Rylle'
witaj(name2)
name3 = 'Ryon'
witaj(name3)