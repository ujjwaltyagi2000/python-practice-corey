if True:
    print("Conditional was True")

user = "Admin"
logged_in = True

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

a=[1,2,3]
b=[1,2,3]

# difference between assignment operator (==) and is operator
print(a==b)
print(a is b)
print("Why does it happen?")
print(id(a))
print(id(b))

c=[4,5,6]
d=c
print(c==d)
print(c is d)
print("Here d and c are the same objects in memory")
print(id(c))
print(id(d))

# examples of what python evaluates to true or false:

# False values:
    # False
    # None
    # Zero of any numeric type (any other number evaluates to True)
    # Any empty sequence (lists, strings, tuples), for example: '', (), []
    # Any empty mapping (dictionary) for example: {}

condition = []

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

