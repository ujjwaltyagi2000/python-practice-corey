'''
The concept of scope rules how variables and names are looked up in your code. 
It determines the visibility of a variable within the code.'''

'''
LEGB
Local, Enclosing, Global, Built-In
'''

# local --> variables defined within a function
# enclosing --> variables in the local scope of enclosing functions (only exists for nested functions)
# global --> variables at the top level of the module
# built-in --> pre-assigned names in python

# LEGB is the order Python follows when resolving names in a program.

x = 'global x' # global variable beccause it is in the main body of our python file

def test():
    y = 'local y'
    print(y)
    print(x)

test()
'''
here the python interpreter first looks for y within the local scope (inside the function).
as for x, it is not found in the local scope. it then looks for x in the enclosing scope.
as there is no nested function, it looks for x in the global scope
'''

# print(y) --> NameError: name 'y' is not defined
# y is a local variable so it cannot be called outside the function

print(x) # works within the function and outside the function

# TESTING THE LEGB RULE:
print("\nTESTING THE LEGB RULE:")
a = 'global a'

def new_test():
    a = 'local a'
    print(a)

new_test() # prints 'local a' as python first looks for a within the local scope and not the global scope
print(a) # prints 'global a'

# CHANGING GLOBAL VALUE WITHIN A FUNCTION:
print("\nCHANGING GLOBAL VALUE WITHIN A FUNCTION:")
i = 'global i'

def change_scope():
    global i
    i = 'local i' # changes the value of global i

change_scope()
print(i) # prints 'local i'

# it's not recommended to use the global statement

# ARE ARGUMENTS LOCAL OR GLOBAL?
print("\nARE ARGUMENTS LOCAL OR GLOBAL?")
def ntest(z):
    print(z)

ntest('local z')
# print(z) --> NameError: name 'z' is not defined
# this is because 'local z' is just an argument and not a declaration on a global scope. so z only exists within the function

# built-in scope
print("\nbuilt-in scope:")

m= min([5,1,2,3,4]) # this will work
print(m)
# min is a built-in function

print(f"Here is the entire list of built-ins:{dir(__builtins__)}")

# python doesn't stop us from writing a function with the same name as a built-in

def min():
    pass

# a = min([5,1,2,3,4])
# print(a) # this will throw an error as it is using the min() function we defined just above it

# ENCLOSING SCOPE:
print("\nENCLOSING SCOPE:")
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        # if you comment the above value it will print 'outer x' two times
        print(f"Value of x within inner() is: {x}")

    inner()
    print(f"Value of x within outer() is: {x}")

outer()