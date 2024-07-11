# dictionaries are similar to hashmaps as they store data in key-value pairs
# dictionaries are mutable 
# dictionaries are unordered

# creating a dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

# accessing values
print(student['name'])
print(student['courses'])

# the keys can be of any other data type too

print("\nAccessing values using get method:")
# the problem with student['name'] is that if the key doesn't exist, it will throw an error
# to avoid this, we can use get method
print(student.get('name'))
print(student.get('phone', 'Not Found'))
# if 'Not Found' is not specified, it will return None
print(student.get('roll_no'))

# adding key and value to a dictionary
print("\nadding key and value to a dictionary:")
student['phone'] = '555-5555'
print(student)

# updating dictionary
print("\nupdating dictionary:")
student['name'] = 'Jane'
print(student)

# update() method:
print("\nupdate() method:")
student.update({'name': 'Jane', 'age': 26})
print(student)
# other key value pairs will remain unchanged

# removing key and value from dictionary
print("\nremoving key and value from dictionary:")
student.pop('age')
print(student)
# if the key doesn't exist, it will throw an error
# to avoid this, use popitem() method   
print(student.popitem())
print(student)

# looping through keys and values:
print("\nlooping through keys and values:")

# looping through keys
for key in student:
    print(key)

# looping through values
for value in student.values():
    print(value)
    # or
# for key in student:
#     print(student[key])

# looping through keys and values
for key, value in student.items():
    print(key, value)

# dictionary comprehension
print("\ndictionary comprehension:")
squares = {x: x**2 for x in range(10)}
print(squares)