# arithmetic operators
print("\n----- Arithmetic -----")
x = 10
y = 3

print(x + y)   # Output: 13
print(x - y)   # Output: 7
print(x * y)   # Output: 30
print(x / y)   # Output: 3.3333333333333335
print(x % y)   # Output: 1
print(x ** y)  # Output: 1000
print(x // y)  # Output: 3

# comparison operators
print("\n----- Comparison -----")
x = 5
y = 10

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True

# logical operators
print("\n----- Logical -----")
x = 5
y = 10

print(x > 0 and y < 20)     # Output: True
print(x > 0 or y < 5)       # Output: True
print(not(x > 0 and y < 5))  # Output: True


# if statements
print("\n----- IF -----")
age = 20
if age >= 18:
    print("You are an adult")

# else statements
print("\n----- ELSE -----")
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# else-if statements
print("\n----- ELSE-IF -----")
score = 85
if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
else:
    print("You need to improve")

