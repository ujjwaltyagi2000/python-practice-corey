import random
import time
import psutil  # Import the psutil module
import os

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# Function to get memory usage
def memory_usage_psutil():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / (1024 * 1024)  # Convert bytes to MB
    return mem

# list comprehension
def people_lists(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

# generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

print(f"Memory (Before): {memory_usage_psutil()} MB")

# using list
# t1 = time.perf_counter()  # Use time.perf_counter() for high precision
# people = people_lists(1000000)
# t2 = time.perf_counter()

# using generator
t1 = time.perf_counter()  # Use time.perf_counter() for high precision
people = people_generator(1000000)
# people = list(people_generator(1000000))
# if you convert a generator into a list it takes the same space and time as before
t2 = time.perf_counter()

print(f"Memory (After): {memory_usage_psutil()} MB")
print(f"Time: {t2 - t1} seconds")

# you'll observe the generator takes almost no space as it doesn't hold anything in memory