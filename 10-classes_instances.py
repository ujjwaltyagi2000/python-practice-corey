# object oriented programming

# why use classes?
''' 
they allow us to logically group our data and functions in a way that's easy to reuse,
and also easy to build upon if need be
'''

# Class:
'''
    > Think of a class as a blueprint or a template. It defines a type of object but doesn't create one itself.
    > For example, if you want to build several houses, you would start with a blueprint that shows the design and structure of the house.
'''

# Object:
'''
    > An object is an instance of a class. It's like using the blueprint to build an actual house.
    > For example, if you have a House class (blueprint), you can create several House objects (actual houses) from it.
'''

# Attributes:
'''
    > Attributes are the characteristics or properties of an object.
    > Continuing with the house example, attributes could be things like the number of rooms, color, size, etc.
    > In code, if you have a House class, an attribute could be self.rooms to store the number of rooms.
'''

# Methods:
'''
    > Methods are actions or functions that an object can perform.
    > For the house, a method could be something like open_door() or paint(color).
    > In code, a method in the House class could look like def open_door(self):.

'''

# Summary:
'''
attribute --> data associated with a class
method --> function associated with a class
object --> instance of a class
class --> blueprint for an object, user-defined data type
'''
# example --> Labrador is an object of class Dog

# creating a class
print("\nCreating a class Employee:")

# blueprint of what an employee should look like
class Employee:
    pass

emp_1 = Employee()
# instance of the employee
emp_2 = Employee()
# second instance of the employee

# so by creating the class Employee once, we can create as many employees (or objects) we want

print(emp_1)
print(emp_2)

emp_1.first = "Ujjwal"
emp_1.last = "Tyagi"
emp_1.email = "ujjwaltyagi@gmail.com"
emp_1.pay = 50000

emp_2.first = "Shrey"
emp_2.last = "Dhawan"
emp_2.email = "shreydhawan@gmail.com"
emp_2.pay = 60000

# manually created objects
print("\nManually created objects:")
print(emp_1.email)
print(emp_2.email)

# here we created two objects of the class Employee
# we want to set all of this for each employee when it's created, instead of doing it manually. It's no different from creating n number of variables

class Worker():
    # __init__ method is a constructor that is called when an object is created
    # it sets the initial state of the object
    def __init__(self, first, last, pay):
        # when we create methods within a class, the receive the instance as the first argument automatically
        # by convention we call the instance self
        # comment this code out and use the later __init__ method too see if it changes things
        
        self.first = first # sets the first name of the instance of worker as 'first' --> the argument that is being passed
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        
        # this is also correct -->
        # self.name = first # sets the first name of the instance of worker as 'first' --> the argument that is being passed
        # self.surname = last
        # self.salary = pay
        # self.email = first + '.' + last + '@gmail.com'


    # def __init__(instance, first, last, pay):
    #     instance.first = first  
    #     instance.last = last
    #     instance.pay = pay
    #     instance.email = first + '.' + last + '@gmail.com'

    # even this __init__ method works fine where we don't use self. but it's convention and therefore a good practice to use self
    
    def full_name(self): # don't forget to pass self as an argument
        return '{} {}'.format(self.first, self.last)
        # here self is passed as an argument as it contains the value we need

# calling the __init__ method
print("\nCalling the __init__ method:")
emp_3 = Worker('Anshuman', 'Pandey', 70000) # __init__ method is called when an object is created
emp_4 = Worker('Siddhant', 'Jha', 80000)
# emp_5 = Worker() # this will throw an error

print(emp_3.full_name())
print(emp_3.email)
print(emp_4.full_name())
print(emp_4.email)

# using class to call methods
print("\nUsing class to call methods:")
print(Worker.full_name(emp_3))
# this syntax isn't used much but it isn't wrong either