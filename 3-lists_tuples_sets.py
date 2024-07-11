# lists and tuples allow us to work with sequential data
# sets are unordered collections of unique elements (no duplicates)

# lists
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[3]) 
# if length of array is n, the last element is array[n-1]
# if index > len(list), IndexError: list index out of range
# if index < 0, IndexError: list index out of range

# negative index:
print("\nNegative Index:")
print(courses[-1]) # in negative index, -1 is the last element
# in negative index, n is the index from the end of the array
# a negative index can go upto [-len(list)], beyond that it gives IndexError

# slicing
print("\nSlicing:")
print(courses[0:2]) # from index 0 to 1
print(courses[:2]) # from index 0 to 1
print(courses[2:]) # from index 2 to the end
print(courses[-3:]) # from index -3 to the end

# list methods:
print("\nList Methods:")
courses.append('Art')
print(courses)
courses.insert(0, 'Language') # insert at index 0
print(courses)
courses2 = ['Music', 'Art']
courses.extend(courses2) # add list to list
print(courses)
courses.remove('Art') # remove element from list
print(courses)
courses.pop() # remove last element
print(courses)
popped = courses.pop()
print(popped)
courses.reverse() # reverse the list
print(courses)
courses.sort() # sort in ascending order
print(courses)
courses.sort(reverse=True) # sort in descending order
print(courses)

# the sort() method changes the list, but what if you don't wish to change the list?
# you can use sorted() function
print(sorted(courses))
print(sorted(courses, reverse=True))

# finding values:
print("\nFinding Values:")
print(f"CompSci is at index: {courses.index('CompSci')}")
print(f"Is Math in courses: {'Math' in courses}")
print(f"Is Science in courses: {'Science' in courses}")

# iterating through a list:
print("\nIterating through a list:")
for course in enumerate(courses, start=1): # returns index and value 
    print(course)

# print list as a string
print("\nList as a String:")
course_str = ', '.join(courses)
print(course_str)

# converting string to list
print("\nString to List:")
course_list = course_str.split(', ')
print(course_list) 

# list comprehension
print("\nList Comprehension:")
squares = [x**2 for x in range(10)]
print(squares)
print([x for x in range(10) if x % 2 == 0])
print([x.upper() for x in courses])
print(['Even' if x % 2 == 0 else 'Odd' for x in range(10)]) # if x is even, 'Even', else 'Odd'  


# tuples
# tuples are immutable
# tuples are faster than lists
print("\nTuples:")
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)
# if you change the value of list_1, list_2 also changes
print(list_1 is list_2) # is checks if the two objects are the same object
print(list_1 == list_2) # == checks if the values are the same

tuple_1 = tuple(courses) # convert list to tuple
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0]= "History"
# TypeError: 'tuple' object does not support item assignment
print(tuple_1 is tuple_2)

# sets
# sets are unordered collections of unique elements
print("\nSets:")
set_1 = set(courses)
print(courses)
print(set_1)
# order of items will be different in both
# after every re-run the order will be different in the set 

# membership test:
print('Math' in courses)
# you can check this with lists too but sets are optimized for it
art_courses = {'History', 'Art', 'Design', 'Design'}
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(art_courses) # it will only print Design once
print(cs_courses.difference(art_courses))
print(art_courses.difference(cs_courses))

# union
print(cs_courses.union(art_courses))
# intersection
print(cs_courses.intersection(art_courses))

# create empty lists, sets, and tuples
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # this is wrong as it is a dictionary
empty_set = set()