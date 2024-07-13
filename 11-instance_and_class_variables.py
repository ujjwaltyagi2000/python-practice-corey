# class variables:
'''
> variables that are shared across all instances of a class
> instance variables are different for each instance of a class, but they share the same class variables
'''

# what data can we have in this class that will be shared by all the instances of this class?
# let's add annual raise as a class variable:

class Employee:

    num_emps = 0
    raise_amt = 1.04 # class variable
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_emps += 1
        # everytime an instance is called, this class variable increases by 1
        # here we didn't write self.num_emps += 1 because num_emps is a class variable and self.num_emps is an instance variable would be an instance variable

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        # we could have written this as: self.pay = int(self.pay * 1.04)
        # but this isn't very convenient as we won't be able to access the raise amount value if we wanted to

        # we can also call raise_amt by writing Employee.raise_amt instead of self.raise_amt

emp_1 = Employee('Ujjwal', 'Tyagi', 50000)
emp_2 = Employee('Shrey', 'Dhawan', 60000)

print("\nOriginal Pay:")
print(emp_1.pay)
print("\nApplying Raise:")
emp_1.apply_raise()
print(emp_1.pay)

# accessing raise amount:
print("\nAccessing Class Variable:")
print(Employee.raise_amt)
print(emp_1.raise_amt)

print("\n")
print(emp_1.__dict__)
print("The instance doesn't contain the raise amount\n")
print(Employee.__dict__)
print("The class contains the raise amount. This is where the instance get its raise_amt value from.")

# changing raise amount:
print("\nChanging Class Variable:")
Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)

print("\nChanging Class Variable using instance:")
emp_1.raise_amt = 1.03 # only changes raise_amt for this instance
print(Employee.raise_amt)
print(emp_1.raise_amt)
# it doesn't affect the class variable, it only affects the instance variable

print(f"Total Number of Employees: {Employee.num_emps}")