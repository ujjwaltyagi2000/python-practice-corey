# inheritance:

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

# let's we want to create different types of employees: developers and managers
# we'll create two new classes called Developer and Manager that will inherit from Employee class but it won't affect the parent class in any way

class dev(Employee): # it is inheriting from Employee class
    raise_amt = 1.10


dev_1 = dev("Ujjwal", "Tyagi", 50000)
dev_2 = dev("Shrey", "Dhawan", 60000)

# now we have two developers
print("\nDevelopers created without writing a single line of code withing class dev:\n")
print(dev_1.email)
print(dev_2.email)

# without writing a single line of code within class dev, we have acquired functionality of Employee

# when dev_1 = dev(*args) is called, it will try to call the __init__ method of dev class
# since there is no __init__ method within dev class, it will try to call the __init__ method of Employee class

# print(help(dev)) # this gives all the info regarding dev class

print(f"\nCurrent pay of {dev_1.full_name()}: {dev_1.pay}")
dev_1.apply_raise()
print(f"\nPay of {dev_1.full_name()} after applying raise: {dev_1.pay}")
# this doesn't change the raise amount of parent class
print(f"\nEmployee raise amount is : {Employee.raise_amt}")
print(f"dev raise amount is : {dev.raise_amt}")


# let's now create a proper Developer class:
class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
         
         super().__init__(first,last,pay) # this will call the __init__ method of Employee class
         # or you can write this: Employee.__init__(self, first, last, pay)
         # using super() is not mandatory but it is a good practice
         self.prog_lang = prog_lang

dev_3 = Developer("Anshuman", "Pandey", 70000, "JS")
print(f"Object created using Developer class: {dev_3.__dict__}")


class Manager(Employee):

    # let's give the option of passing in a list of employees that this manager supervises
    def __init__(self, first, last, pay, employees = None):
       
        #  avoid passing mutable items like lists as default values
       
         super().__init__(first,last,pay)
         
         if employees is None:
             self.employees = []
         else:
             self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"{self.full_name()} is supervising:")
            print('-->', emp.full_name())

print("\nManager class created using inheritance from Employee class:\n")
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])
mgr_2 = Manager("Bob", "Smith", 90000, [dev_2, dev_3])

mgr_1.print_emps()
mgr_2.print_emps()

mgr_2.remove_emp(dev_2)
print("\nAfter removing dev_2 from mgr_2:")
mgr_2.print_emps()

# check if mgr_1 and mgr_2 are instances of Manager class
print("\nIs mgr_1 an instance of Manager class:", isinstance(mgr_1, Manager))
print("Is mgr_1 an instance of Employee class:", isinstance(mgr_1, Employee))
print("Is mgr_1 an instance of Developer class:", isinstance(mgr_1, Developer))

# check if Developer and Manager are subclasses of Employee
print("\nIs Developer a subclass of Employee class:", issubclass(Developer, Employee))
print("Is Manager a subclass of Employee class:", issubclass(Manager, Employee))