# Closures

'''
A closure is a record storing a function together an environment: a mapping associating each free variable
of the function with the value or storage location to which the name was bound when the closure was created.
A closure, unlike a plain function. allows the function to access those captured variables through the 
closure's reference to them, even when the function is invoked outside their scope.
'''

def outer_func(msg):
    message = msg

    def inner_func():
        print(message) 
        # message is a free variable as it isn't defined within the scope of this function

    # return inner_func() 
    # This would execute the inner_func immediately and return the result of that execution
    
    return inner_func
    # This returns the function object inner_func itself without executing it. This allows you to store inner_func in a variable (my_func in this case) and call it later.

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')
print(hi_func.__name__) # prints 'inner_func' when you use the second return statement as that returns a function object
print(hi_func) 

hi_func()
hello_func()

'''
As observed from the above code, closures in Python help to invoke functions outside their scope. 
The function innerFunction has its scope only inside the outerFunction. 
But with the use of Python closures, we can easily extend its scope to invoke a function outside its scope.
'''