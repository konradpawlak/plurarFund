# classes and objects

# ex. phone ->
# state   | behavior
# ------------------
# Model   | Ringing
# Color   | Reciving notifications
# Storage | Sending data

# ex. dog ->
# state   | behavior
# ------------------
# Name    | Barking
# Breed   | Whining
# Hungry  | Wagging tail

# do a robot dog -> same states and behavior like real one(and example above)

# Robot Dog Class -> class instance -> dog

class Robot_dog:
    def __init__(self, name, breed ): # -> innit metod lets us initialize our robot's properties | slef - always first parametr in an innit, it refers to instance of the class we creating or the current object
        self.name = name              # -> name, breed -> ther values of the properites that we want to innitialize as parameters
        self.breed = breed            # -> initialize the properties of the new objects, selft, to the passed values | PASSed-in parameters have same name as the self objects properties

    def bark(self):                   # -> method of a class acting as behavior
        print('Woof, woof')

# same as:
class Robot_cat:
    def __init__(self, name_cat, bred_cat):
        self.name = name_cat
        self.breed = bred_cat
    def moew(self):
        print('Moew, moew!')

# initialize robots in main function

my_dog = Robot_dog('Spotter','Spaniel') # self is ignored
my_cat = Robot_cat('Dachowiec','Laki')

print(my_dog.name, my_dog.breed)
print(my_cat.name, my_cat.breed)

my_dog.bark()
my_cat.moew()


# add to the class behavior - barking