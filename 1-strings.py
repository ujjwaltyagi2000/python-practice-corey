message="Hello World"
print(message)

# why use double quotes in python? because when you write a string within single quotes you end up with this problem:
# SyntaxError: unterminated string literal
# print('Ujjwal's World')

# to avoid this, use '\' to escape the single quote
print('Ujjwal\'s World')
# or simply use double quotes when using single quotes in the string

# similiarly use single quotes outside when using double quotes within the string
# example:
print('he said "hello"')

# print multiple line string
new_message = """
Hello
World
"""
print(new_message)

# length of string:
print(len(message))

# accessing string characters individually:
print("\naccessing string characters:")
print(message[2])
print(message[-1])

# slicing strings:
print("\nString Slicing:")
print(message[0:5])
print(message[:5]) # doesn't include the 5th index
print(message[6:]) # includes the 6th index

# string methods:
print("\nString Methods:")
print(message.lower())
print(message.upper())
print(message.find("World")) # returns index where string is found, -1 if not found
print(message.replace("World", "Universe"))
print(message.count('l'))
print(message.count('World'))

# concatanating strings:
print("\nConcatenating Strings:")
greeting = "Hello"
name = "Ujjwal"
text = greeting + " " + name
print(text)

# formatting strings:
print("\nFormatting Strings:")
name = "Ujjwal"
age = 23
print("My name is " + name + " and I am " + str(age) + " years old.")

# f-string:
print("\nf-string:")
print(f"My name is {name.upper()} and I am {age} years old.")

# dir:
print("\ndir():")
print(dir(name))
# the dir() method returns all the methods and attributes of the object

# help:
print(help(str.lower))
