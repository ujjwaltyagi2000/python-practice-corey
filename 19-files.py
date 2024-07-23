# file objects
print("\nfile objects:")
f = open("test.txt", "r") # open file in read mode
print(f.name)
print(f.read()) # read all the data in the file
f.close() # close the file

'''
method to work with a file:
> open it
> select mode --> read, write, append
> read/write data
> close the file
'''

# why close file?
'''
In Python, the close() method is used to close a file and free up any system resources that were used during the file operation. 
This method is called on a file object, which is created when a file is opened.

When you’re done with a file, it’s good practice to close it. 
Not closing a file can lead to memory leaks, meaning your program continues to consume memory space even though it’s no longer needed. 
This can slow down your program and, in worst-case scenarios, cause your program to crash.
'''

# or you can do it with the help of with statement
print("\nwith statement:")
with open("new_test.txt", "r") as f:
    f_contents = f.read()
    print(f_contents)

'''
A context manager in Python is an object that is used to manage resources with a defined setup and cleanup process, ensuring that resources are properly acquired and released. 
It is most commonly used with the with statement to encapsulate operations that need to be managed, such as opening and closing files, acquiring and releasing locks, or establishing and closing database connections.
'''
print("\nreadline():")
with open("new_test.txt", "r") as f:
    f_contents = f.readline()
    print(f_contents, end='') # prevents new line
    f_contents = f.readline()
    print(f_contents, end='') 

print("\nreading lines using iterator:")

with open('test.txt', 'r') as f:
    for line in f:
        print(line)

print("\nPrinting n number of characters from the file:")

with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents)   
    f_contents = f.read(100)
    print(f_contents)
    f_contents = f.read(100) # this will give an empty string
    print(f_contents)