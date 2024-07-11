num = 3
print(type(num))
f_num = 3.14
print(type(f_num))

print("\nArithmetic Operations:")
a=5
b=2
print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a+b}")
print(f"a - b = {a-b}")
print(f"a * b = {a*b}")
print(f"a / b = {a/b}") # floating point division
print(f"a // b = {a//b}")  # integer division/floor division
print(f"a % b = {a%b}")  # modulus
print(f"a ** b = {a**b}") # exponent

# abs():
print(abs(-10))

# round():
print(round(3.14)) # round to the nearest whole number
print(round(3.56)) # round to the nearest whole number
print(round(3.566,1)) # round to 1 decimal place

# type conversion:
print("\nType Conversion:")
num_1 = '100'
num_2 = '200'
print(f"num_1 = {num_1} and type of num_1 = {type(num_1)}")
print(f"num_2 = {num_2} and type of num_2 = {type(num_2)}")
print(f"num_1 + num_2 = {num_1+num_2}")
print(f"After type conversion, num_1 + num_2 = {int(num_1) + int(num_2)}") # string casted as integer