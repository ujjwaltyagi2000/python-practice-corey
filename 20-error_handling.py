# try, except, else, finally

'''
An Exception is an Unexpected Event, which occurs during the execution of the program. It is also known as a run time error. 
When that error occurs, Python generates an exception during the execution and that can be handled, which prevents your program from interrupting.
'''

# now it is helpful for developers but it also stops the entire code from running
# to deal with this and make sure the code doesn't break in production, we use try except for error handling

# here is the general syntax: 

try:
       # Some Code.... 
       pass
except:
       # optional block
       # Handling of exception (if required)
       pass
else:
       # execute if no exception
       pass
        # The other optional clause is the else clause. 
        # The else clause is simple: if the code in the try clause executes without throwing an error, then the code in the else clause will also execute.
finally:
      # Some code .....(always executed)
        # The finally clause will always execute, whether there is an error or not.
      pass

# example:

def divide(x, y): 
    try: 
        # Floor Division : Gives only Fractional 
        # Part as Answer 
        result = x // y 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
    else:
        print(f"{x} // {y} = {result}") 
    finally:  
        # this block is always executed   
        # regardless of exception generation.  
        print('This is always executed')   

# Look at parameters and note the working of Program 
divide(3, 2) 
divide(3, 0)

# it's not necessary that you use else and finally block, most cases only require the use of try and except 

'''
If the code in the try clause does throw an exception and the type of exception is specified after any except keyword, the program will:

    > Skip the remaining code in the try clause
    > Execute any code in the matching except clause
    > Continue running as normal
'''

'''
Errors in the Try Clause and the Exception is not Specified

Finally, if the program throws an exception in the try clause, but the exception is not specified in any except statements, 
then the program will stop the execution of the program and throw the error
'''

x = 0
try:
    print(5 / y)
except:
    print("Something went wrong")

print("I am executing after the try clause!")

# NameError: name 'y' is not defined

# # built in exceptions:
#     KeyError – A key cannot be found in a dictionary
#     IndexError – The index is out-of-bounds on an iterable object
#     TypeError – A function or operation was used on the wrong type of object
#     OSError – General operating system errors