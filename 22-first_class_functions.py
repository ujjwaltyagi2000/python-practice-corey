# first class functions
# A programming language is said to have first class functions if it treats functions as first-class citizens

'''
First Class citizens in programming:
A first class citizen (or first-class objects) in a programming language is an entity which supports all the
operations generally available to other entities. These operations typically include being passed as an argument,
returned from a function, and assigned to a variable.

'''

# Python supports the concept of First Class functions.

# this is what we are used to do with functions:
def square(x):
    return x*x

# calling the function
f = square(5)

# now let's try assigning a function to a variable
j = square 

print(square) #<function square at 0x0000024EAD083E20>
print(f) # 25
print(j(6)) # it prints 36 as it is a function now

'''
Properties of first class functions:

>    A function is an instance of the Object type.
>    You can store the function in a variable.
>    You can pass the function as a parameter to another function.
>    You can return the function from a function.
>    You can store them in data structures such as hash tables, lists, …

'''

# passing function as an argument to another function

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5]) # don't write square() as then the program will try to run the function

print(squares)

# what's the benefit of this?

# now we can pass any function as an argument to our map function

# example:
def cube(x):
    return x*x*x

cubes = my_map(cube, [1,2,3,4,5])

print(cubes)

# another example:
def logger(msg):
    def log_message():
        print('Log: ', msg)
    log_message()
    return log_message

log_hi = logger('Hi!') # logger returns log_message() and prints 'Log: Hi!'
# log_hi()

# how is it useful?

def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!') # print_h1 is now a function that prints <h1>
print_h1('Another Headline!')

print_p = html_tag('p') # print_p is now a function that prints <p>
print_p('Test Paragraph!')