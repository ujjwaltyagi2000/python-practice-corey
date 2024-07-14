# special methods, also known as magic methods or dunder methods

'''
A special method is a method whose name starts and ends with a double underscore. 
These methods have special meanings for Python.
Python automatically calls magic methods as a response to certain operations, such as instantiation, sequence indexing, attribute managing, and much more. 
'''

# __init__ --> pronounced as dunder init

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):

        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Ujjwal', 'Tyagi', 50000)
emp_2 = Employee('Shrey', 'Dhawan', 60000)

# one way of calling __repr__ or __str___
print(repr(emp_1))

# other method to write __repr__ or __str__
print(emp_1.__str__())

# In Python, the str() and repr() functions are used to obtain string representations of objects. 
# While they may seem similar at first glance, there are some differences in how they behave. 
# Both of the functions can be helpful in debugging or printing useful information about the object.

# __str__ --> Returns a human-readable string representation of the object

# __repr__ --> Returns a developer-readable string representation of the object
# __repr__ is used for debugging purposes and __str__ is used for end users

# __str__ and __repr__ are both called when you print or use the print() function

'''
basically write __repr__ such that it represents the object in a developer friendly way, conveying all the necessary info about the object

and, write __str__ such that it represents the object in a user friendly way
'''

# adding salaries of two employees using __add__ dunder: 
print(f"\nSum of salaries of {emp_1.full_name()} and {emp_2.full_name()} calculated using __add__is: {emp_1+emp_2}")

# the __add__ method is called when you use the + operator on two objects

# here you specified in the __add__ that if two objects are added using the '+' operator, then return the sum of their pay

# __len__ dunder: 
print(f"\nLength of {emp_1.full_name()} calculated using __len__ is: {len(emp_1)}")

# the __len__ method is called when you use the len() function on an object