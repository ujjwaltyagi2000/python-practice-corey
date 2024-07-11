import timeit

# Function to test appending to a list
def test_list_append():
    lst = []
    for i in range(1000):
        lst.append(i)

# Function to test appending to a tuple (not possible directly, so we simulate by creating a new tuple)
def test_tuple_append():
    tpl = ()
    for i in range(1000):
        tpl = tpl + (i,)

# Function to test accessing elements in a list
def test_list_access():
    lst = list(range(1000))
    for i in range(1000):
        _ = lst[i]

# Function to test accessing elements in a tuple
def test_tuple_access():
    tpl = tuple(range(1000))
    for i in range(1000):
        _ = tpl[i]

# Function to test creating a list
def test_list_creation():
    lst = [i for i in range(1000)]

# Function to test creating a tuple
def test_tuple_creation():
    tpl = tuple(i for i in range(1000))

# Timing the functions
list_append_time = timeit.timeit(test_list_append, number=1000)
tuple_append_time = timeit.timeit(test_tuple_append, number=1000)
list_access_time = timeit.timeit(test_list_access, number=1000)
tuple_access_time = timeit.timeit(test_tuple_access, number=1000)
list_creation_time = timeit.timeit(test_list_creation, number=1000)
tuple_creation_time = timeit.timeit(test_tuple_creation, number=1000)

# Printing the results
print(f"List append time: {list_append_time:.6f} seconds")
print(f"Tuple append time: {tuple_append_time:.6f} seconds")
print(f"List access time: {list_access_time:.6f} seconds")
print(f"Tuple access time: {tuple_access_time:.6f} seconds")
print(f"List creation time: {list_creation_time:.6f} seconds")
print(f"Tuple creation time: {tuple_creation_time:.6f} seconds")
