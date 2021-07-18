#######################################################
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hello, my name is %s" % self.name)


#######################################################
p1 = Person("Nina", 21)
print(p1.name)
print(p1.age)
p1.introduce()
