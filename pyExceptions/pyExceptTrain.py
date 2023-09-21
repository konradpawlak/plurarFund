# this one will show try/except on dictionary key error
acronyms = {
    'KEK':"better than lul",
    'LUL':"better than lol",
    'Pog':"hype ongoing",
    '4Head':"giga brain omegalul",
    'Kappa':"naxx out??",
}

try:
    definition = acronyms['Sadeg']
    print('Definition of', acronyms['Sadeg'], 'is', definition)
except:
    print('Sorry mordo, ni ma takiej emoty w bazie')
finally: # executed always no matter if try block raised an error or not
    print('The acronyms we have defined are:')
    for acronym in acronyms:
        print(acronym)

try:
    definition1 = acronyms['4Head']
except:
    print('Sorry mordo, ni ma takiej emoty w bazie')
else:
    print(definition1)

print('the program keep going....') # if there are no error thats were left unexpected