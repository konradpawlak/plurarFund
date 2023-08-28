print("empty list")
acronyms = []
print(acronyms)
acronyms.append('LOL')
acronyms.append('KEK')
acronyms.append('OMEGA')
acronyms.append('IDK')
acronyms.append('FYI')
print("full list")
print(acronyms)
del acronyms[4]
print("deleted FYI from the list")
print(acronyms)
acronyms.append('FYI')
print("aded FYI to the list")
print(acronyms)

for acronym in acronyms:
    print(acronym)