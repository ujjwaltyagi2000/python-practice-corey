# property decorators:

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    
emp_1 = Employee('Ujjwal', 'Tyagi', 50000)

emp_1.first = "Shrey"
print(emp_1.first)
print(emp_1.full_name())
print(emp_1.email)
# the email still gives Ujjwal.Tyagi@gmail.com as output
# to fix this we can use the property decorator

# we could write an e_mail method too but if this code is being used at multiple places, this change would break the code 
# this is because everywhere the email being used would be an attribute so it must be changed to a method everywhere it is being used

# we can use the property decorator to fix this

# let's rewrite the class:
class Worker:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    
        self.pay = pay
        # self.email = first + '.' + last + '@gmail.com'
        # delete the email attribute and use the property decorator

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
new_emp = Worker('Siddhant', 'Jha', 50000)

# now we can use the email attribute
print("\nUsing the property decorator:")
new_emp.first = "Shrey"
print(new_emp.first)
print(new_emp.email)
print(new_emp.full_name) # full name is now an attribute too

# say now we want this:
# new_emp.full_name = "Siddhant Jha" to change both the first and last name
# but this will throw an error. how do we fix this?

# we can use the setter decorator
# let's rewrite the class:  

class newWorker:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    
        self.pay = pay
        # self.email = first + '.' + last + '@gmail.com'
        # delete the email attribute and use the property decorator

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("\nDeleting Name")
        self.first = None
        self.last = None

# now if we try to set the full_name:

new_emp = newWorker('Siddhant', 'Jha', 50000)
print(f"\nOriginal Name of the employee: {new_emp.full_name}")
new_emp.full_name = "Ujjwal Tyagi"
print(f"New Name of the employee: {new_emp.full_name}")

# using deleter
del new_emp.full_name
print(f"New Name of the employee: {new_emp.full_name}")