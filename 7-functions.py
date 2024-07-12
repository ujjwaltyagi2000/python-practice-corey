# functions:
# some instructions packaged together that perform a specific task
# functions are defined using def keyword
# functions are called using the name of the function

# defining a function:
def hello_func():
    pass
# pass keyword is used to write empty functions

# calling a function:
hello_func()

def greet():
    return "Hello"
    # print("Hello") you can use this also for simple task of printing but we usually return values to be used by some other function

# printing a function:
print(greet) # prints the memory address of the function
print(greet()) # prints the result of the function (in this case None)
# if greet() had print() we wouldn't need to use print(greet()), it would automatically print "Hello" upon execution

# benefits of functions:
# 1. reusability
# 2. code organization
# 3. code readability
# 4. code maintenance
# 5. code modularity

# example:
def add(num1, num2):
    return num1 + num2
# num1 and num2 are parameters

print(add(5, 10))
# 5 and 10 are arguments

# the difference between parameters and arguments:
# parameters are the variables in the function definition
# arguments are the values passed to the function when it is called

# adding functionality to a function:
print(greet().upper())

# setting a default parameter
# if a parameter is not passed, it will take the default value
def multiply(a,b=5):
    return a*b

print("output with two arguments:")
print(multiply(5, 10))

print("output with one argument:")
print(multiply(5))

# *args and **kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='John', age=22)
# *args and **kwargs allow us to pass multiple arbitrary arguments to the function
# you don't have to use the words args and kwargs, but it is good practice to do so
# *args allows us to pass any number of positional arguments
# **kwargs allows us to pass any number of keyword arguments
# we can pass both at the same time by using *args and **kwargs

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# passing courses and info as positional arguments:
print("\npassing courses and info as positional arguments:")
student_info(courses, info) 
# here the courses and info are received as args as their own data type, the kwargs remain empty

# passing courses as positional arguments and info as keyword arguments:
print("\npassing courses and info as multiple arbitrary arguments")
student_info(*courses, **info)
# here courses is received as args and info is received as kwargs

# if you would have passed the arguments as student_info(courses,info), it would have taken the arguments as a list and a dictionary respectively
# this way we passed courses and info as multiple arguments, both positional and keyword

# example:
print("\nExample to determine the number of days in a month given a year is given:")
months_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 0 is just a placeholder that won't be used (it just covers the 0th index)

def is_leap_year(year):
    # return True for leap years and False for non-leap years
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return "Invalid month"
    if month == 2 and is_leap_year(year):
        return 29
    return months_days[month]

year = 2020
month = 2
print(f"Year = {year}, Month = {month}")
print(f"Number of days = {days_in_month(year, month)}")
