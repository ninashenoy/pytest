###########################################################################
def hello_world():
    print("Hello World")

###########################################################################
def hello(name):
    print("Hello %s" % name)

###########################################################################
def list_names(*names):
    for n in names:
        print(n)

###########################################################################
def welcome(place="America"):
    print("Welcome to " + place)

###########################################################################
def print_list(list):
    for item in list:
        print(item)
    
############################################################################
def addition(x,y):
    sum = x+y
    print("The sum of %i and %i is %i" % (x, y, sum))
    return sum

############################################################################
hello_world()
hello("Shadow")

# If you do not know how many arguments will be passed into the function,
# ...Add a * before the parameter name in the function definition
list_names("Nina", "Shadow", "Leo")

# When you set a default parameter argument in a function, then when the function
# is called without any arguments, then it will substitute the default
welcome("India")
welcome("Canada")
welcome()

fruits = ["apple", "banana", "orange"]
print_list(fruits)

s = addition(3,5)
print(s)


