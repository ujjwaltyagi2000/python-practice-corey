# Python Assertions in any programming language are the debugging tools that help in the smooth flow of code. 
# Assertions are mainly assumptions that a programmer knows or always wants to be true and hence puts them in code so that failure of these doesn’t allow the code to execute further. 

# In simpler terms, we can say that assertion is the boolean expression that checks if the statement is True or False. 
# If the statement is true then it does nothing and continues the execution, 
# but if the statement is False then it stops the execution of the program and throws an error.

# error thrown --> AssertionError

# Syntax : assert condition, error_message(optional) 


# example 1

# initializing number
# a = 4
# b = 0
 
# # using assert to check for 0
# print("The value of a / b is : ")
# # the code won't execute after this line if the below assertion is raised:
# assert b != 0

# # you can also add an error message like this:
# # assert b != 0, "Zero Division Error" 

# # this line will execute if the above assertion is not raised
# print(a / b)


# example 2


# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    # Assertion to check that the length and width are positive
    assert length > 0 and width > 0, "Length and width"+ \
                "must be positive"
    # Calculation of the area
    area = length * width
    # Return statement
    return area
 
 
# Calling the function with positive inputs
area1 = calculate_rectangle_area(5, 6)
print("Area of rectangle with length 5 and width 6 is", area1)
 
# Calling the function with negative inputs
area2 = calculate_rectangle_area(-5, 6)
print("Area of rectangle with length -5 and width 6 is", area2)
