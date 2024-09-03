def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

print("Using next()")
print(my_nums) # won't print any numbers
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums)) # prints StopIteration

# or
print("\nUsing for loop:")
for num in my_nums:
    print(num)
    # depending upon how many values have already been generated above, the remaining values will be printed here
# nothing is printed when  the generator is exhausted

# generators don't hold the entire list in memory. They generate the list on demand
# generators are iterable

'''
why use generators?

- memory efficient
- better performance

'''

new_nums = [x*x for x in [6,7,8,9,10]] # list comprehension 
print(new_nums)
gen_nums = (x*x for x in [6,7,8,9,10]) # generator
print(gen_nums)

