# Functions
def greet():
    print("Hello, world!")

greet()  # Output: Hello, world!

# Parameters
# (new def = overwrites the previous function)
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # Output: Hello, Alice!


# Return Statements
def add(a, b):
    return a + b
    print("hello") # this will not execute

result = add(3, 4)
print(result)  # Output: 7
