nums = [1,2,3,4,5]

for num in nums:
    print(num)

# break statement:
print("\nbreak statement:")
for num in nums:    
    if num == 3:
        print("Found it!")
        break
    print(num)
# Break statement stops the entire process of the loop. 
# Break also terminates the remaining iterations. 

# continue statement:
print("\ncontinue statement:")
for num in nums:
    if num == 3:
        print("Found it!")
        continue
    print(num)
# Continue statement only stops the current iteration of the loop. 
# Continue doesn't terminate the next iterations; it resumes with the successive iterations.

# nested loop:
print("\ncontinue statement:")
for num in nums:
    for letter in 'abc':
        print(num, letter)  
# loop within a loop

# range function:
print("\nrange function:")
for i in range(1, 11):  # range(1, 11) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(i)


# while loop:
print("\nwhile loop:")
i = 1
while i <= 10:
    print(i)
    i += 1
# the while loop continues until the condition is false

# infinite loop:
# i=1
# while True:
#     print(i)
#     i += 1
# # to break out of it, press ctrl+c 