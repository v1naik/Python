"""
Object Oriented Programming
"""

s = "this is a string" # s is an object of class String
a = "one more string"
s.upper()
s.lower()
print(type('s'))
print(type('a'))
print(type([1, 2, 3]))


# Example 1
class Person:
	pass
p = Person()
print(type(p))



# Example 2
class Car(object):

    def __init__(self, make, model="550i"):
        self.make = make
        self.model = model

c1 = Car('bmw')
print(c1.make)
print(c1.model)
c2 = Car('benz')
print(c2.make)
print(c2.model)
#print(Car.wheels)
#self is a variable in python that is used as the very first argument for every
#function. Not necessary to name it 'self', can be any other name. But let's
# stick with convention


# Example 3
# A User class with 3 attributes but no methods (aside from __init__)
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)




# Example 4
class MyClass:
    name = "Raghav"
    
    #You can also create functions inside class
    def sum(self, a, b):
        print (a+b)

    def __init__(self,name,age):
        self.name = name
        self.age = age

x = MyClass("John", 40)
print(x.name)
x.sum(4,5)
print(x.age)
#del x


# Example 5
class Students:
    # _init_: A Built-in fucntion that is always present. Also called the initialize function
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def displayStudent(self):
        return ("Student name is " + self.name + " and age is " + str(self.age) + " and grade is: " + str(self.grade))

students1 = Students("Bob", 12, "7th")
print(students1.name)
print(students1.age)
print(students1.grade)

Stu = Students("Chad", 15, "A")
print(Stu.displayStudent())

#students2 = Students("Dylan", 14)
#print(students2.name)
#print(students2.age)
#print(students2.grade)



# Example 6 (Inheritance)
class Car(object):

    def __init__(self):
        print("You just created the car instance")
    def drive(self):
        print("Car started...")
    def stop(self):
        print("Car stopped")

class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        Car.drive(self)
        print("You just created the BMW instance")

c = Car()
c.drive()
c.stop()

b = BMW()
b.drive()
b.stop()