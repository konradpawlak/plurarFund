age = int(input("how many decades old are you?\n"))

#decades = age // 10 == same as below
decades = int(age/10)
years = age%10

print(f"you are {decades} decades, and {years} year old bro")

print("you are " + str(decades) +" decades, and " + str(years) + " year old bro")