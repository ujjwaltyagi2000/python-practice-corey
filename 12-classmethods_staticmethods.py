# regular methods, class methods, and static methods -->

# regular methods in a class take the instance as the first argument

# class methods in a class take the class as the first argument

# static methods don't take any arguments automatically, they don't pass the instance or the class
# why are static methods used? because they have some logical connection to the class

class Employee:

    num_emps = 0
    raise_amt = 1.04 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_emps += 1
        
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    # here classmethod is a decorator that alterates the functionality of a method
    def set_raise_amt(cls, amount):
        # here the class variable is referred as cls by convention, it can be called anything else too (except the word 'class' as it is reserved)
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # let's say we want to write a function that takes a date as input and returns whether or not it was a work day
    # we can do it with static methods
    @staticmethod
    def is_workday(day):
        # monday --> 0 and sunday --> 6
        # weekday() returns an integer from 0 to 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Ujjwal', 'Tyagi', 50000)
emp_2 = Employee('Shrey', 'Dhawan', 50000)

emp_1.apply_raise()
print(f"\n{emp_1.full_name()}'s salary is: {emp_1.pay} and the raise amount is: {emp_1.raise_amt}.") # this will print the class variable (raise_amt) as it is not an instance variable (pay)emp_1.pay)

Employee.set_raise_amt(1.05)

emp_2.apply_raise()
print(f"\n{emp_2.full_name()}'s salary is: {emp_2.pay} and the raise amount is: {emp_2.raise_amt}.") # this will print the class variable (raise_amt) as it is not an instance variable (pay)emp_1.pay)

# we can use these classmethods to provide multiple ways of creating objects

# say you receive employee data in the form of strings where each data is separated by hyphens
# and you want to create an object for each employee
# you can do it with the help of classmethods

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# we wish to use these to create 3 new instances

# this is how we would do it:
print("\nInstance created by manually splitting the string:")
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.__dict__)

# now we don't to do this for multiple instances.
# instead, let's just write a method above to do this for us

print("\nInstances created by classmethod:")
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.__dict__)
new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.__dict__)

# using static method:
print("\nUsing Static Method:")

import datetime

my_date = datetime.date(2020, 6, 18)
print(f"Is {my_date} a workday? --> {Employee.is_workday(my_date)}")
