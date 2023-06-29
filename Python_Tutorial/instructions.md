# Python Tutorial

For the sake of efficiency, when learning to code in any language, it is important to focus on the most important concepts that will appear most frequently. 

As such, the following is a Python tutorial based on the Pareto principle (a.k.a the 80/20 rule) which will introduce the top 20% of coding concepts that you will likely use 80% of the time.

**Assumptions:**
- You have Python 3.10 installed via the stand-alone version or through anaconda. 
- You have VS Code installed with the python extension and can run Python with VS Code

**Outline:**
1. [Introduction to Python](#introduction-to-python)
1. [Basic Data Types and Variables](#basic-data-types-and-variables)
1. [Operators and Conditional Statements](#operators-and-conditional-statements)
1. [Loops](#loops)
1. [Containers](#containers)
1. [Functions](#functions)
1. [Libraries](#libraries)
1. [File Input and Output](#file-input-and-output)
1. [Error Handling](#error-handling)
1. [Object-Oriented Programming](#object-oriented-programming)

<br/>

---
# Introduction to Python

<details>
	<summary>
	Expand
	</summary>

Python is a popular and versatile programming language known for its simplicity and readability. It is widely used in various domains, including web development, data analysis, artificial intelligence, and more. In this tutorial, we will cover the fundamental concepts of Python programming and provide you with the knowledge to start writing your own Python code.

- Python is great for code readability. This is because Python code is written in a manner that is very similar to human language. Let's see an example:
    - In VS Code, in the explorer panel (left side), create a new file called `intro.py`
    - Open that file in VS Code and enter the following in the available space and then save the file: 
        ```Python
        print("Hello, World!")
        ```
    - Now, press the "run" button for that file
        - If you have configured VS Code properly and the VS Code Python extension is installed, the "run" button will look like a right-facing arrow in the top-right of your VS Code screen.
    - The output should look like this:
        ```Shell
        Hello, World!
        ```
- When coding, you may want to leave comments for your future self or for someone else reading your code. This is often done to explain what is happening in section of code. Comments are ignored by Python. There are 3 ways to create comments:
    - `Single-line` (very common). Best to place these above code rather than beside it.
        ```Python
        # This is a comment
        print("Hello, World!") # Also a comment (but "Hello, World!" will still print)
        ```
    - `Multi-line`. Often seen when one line is not enough to describe something. 
        ```Python
        '''
        This is a
        Multi-line comment
        '''
        """
        This also works
        """
        print("Hello, World!") 
        ```
    - `Python Docstrings`. These are used to automatically generate documentation about your code. This is a little more advanced, so we will explain this in [Functions](#Functions). For now, here's an example of what it looks like:
        ```Python
        def example():
            """
            This is used when creating documentation to describe a function
            """
        ```




</details>

---
# Basic Data Types and Variables

<details>
	<summary>
	Expand
	</summary>

Before diving into programming concepts, it's essential to understand the basic data types and variables in Python. In this section, we will explore integers, floating-point numbers, strings, booleans, and variables. Understanding these concepts will lay the foundation for more complex programming tasks.

## Variables
- In order to manipulate/produce information with Python, you will typically have to store values in variables.
- To create a variable, you start by specifying the name of the variable followed by an equal sign (=) and then you enter the information you want to be stored. For example:
    ```Python
    # number is the variable name, and 12 is the value stored in the variable
    number = 12
    ```
- Some built-in variable types include:
    - Integers
    - Floating-Point Numbers
    - Strings

- Python has a pre-defined list of ["keywords"](https://docs.python.org/3/reference/lexical_analysis.html#keywords) which are reserved by Python to use in a specific manner. In other words, when Python sees these keywords, it expects to perform a certain action. You cannot use these words as variable names.

## Integers
- Integers are whole numbers without decimal points. In Python, you can assign an integer value to a variable and perform mathematical operations on it.
    ```Python
    num1 = 10
    num2 = 20
    print(num1 + num2)  # Output: 30
    ```

## Floating-Point Numbers (Floats)
- Floating-point numbers, or floats, are numbers that contain decimal points. They are used to represent real numbers in Python.
    ```Python
    float1 = 3.14
    float2 = 2.5
    print(float1 * float2)  # Output: 7.85
    ```

## Strings
- Strings are sequences of characters enclosed in single or double quotation marks. They are used to represent text in Python. 
    ```Python
    string1 = "Hello"
    string2 = "world"
    print(string1 + " " + string2)  # Output: Hello world
    ```
    - Strings are immutable, meaning their elements cannot be modified once defined. If you want to change a character of a string in Python, you have to overwrite the entire string.

## Booleans
- Booleans represent truth values, either True or False. They are used in conditional statements and logical operations.
    ```Python
    is_raining = True
    is_sunny = False
    print(is_raining)  # Output: Hello world
    ```


</details>

---
# Operators and Conditional Statements

<details>
	<summary>
	Expand
	</summary>

Operators are symbols or special ["keywords"](https://docs.python.org/3/reference/lexical_analysis.html#keywords) that perform various operations on values or variables. They allow you to manipulate data, make comparisons, perform mathematical calculations, and more. 

Conditional statements allow our programs to make decisions based on specific conditions. 

In this section, we will cover different types of operators and how to use them in conditional statements.

## Arithmetic Operators
- Arithmetic operators are used to perform mathematical calculations. Python provides the following arithmetic operators:
    - Addition (+): Adds two values.
    - Subtraction (-): Subtracts one value from another.
    - Multiplication (*): Multiplies two values.
    - Division (/): Divides one value by another.
    - Modulus (%): Returns the remainder of the division.
    - Exponentiation (**): Raises a value to the power of another.
    - Floor Division (//): Returns the quotient of the division, rounded down to the nearest whole number.

    ```Python
    x = 10
    y = 3

    print(x + y)   # Output: 13
    print(x - y)   # Output: 7
    print(x * y)   # Output: 30
    print(x / y)   # Output: 3.3333333333333335
    print(x % y)   # Output: 1
    print(x ** y)  # Output: 1000
    print(x // y)  # Output: 3
    ```

## Comparison Operators
- Comparison operators are used to compare values and return a boolean result (True or False). Python provides the following comparison operators:
    - Equal to (==): Checks if two values are equal.
    - Not equal to (!=): Checks if two values are not equal.
    - Greater than (>): Checks if the left value is greater than the right value.
    - Less than (<): Checks if the left value is less than the right value.
    - Greater than or equal to (>=): Checks if the left value is greater than or equal to the right value.
    - Less than or equal to (<=): Checks if the left value is less than or equal to the right value.
    
    ```Python
    x = 5
    y = 10

    print(x == y)  # Output: False
    print(x != y)  # Output: True
    print(x > y)   # Output: False
    print(x < y)   # Output: True
    print(x >= y)  # Output: False
    print(x <= y)  # Output: True
    ```

## Logical Operators
- Logical operators are used to combine multiple conditions and evaluate the overall expression. Python provides the following logical operators:
    - Logical AND (and): Returns True if both conditions are True.
    - Logical OR (or): Returns True if at least one condition is True.
    - Logical NOT (not): Returns the opposite boolean value of the condition.
    
    ```Python
    x = 5
    y = 10

    print((x > 0) and (y < 20))     # Output: True
    print((x > 0) or (y < 5))       # Output: True
    print(not((x > 0) or (y < 5)))  # Output: False
    ```


## IF Statements
- The `if` statement allows you to conditionally execute a block of code if a certain condition is true.
    ```Python
    age = 20
    if age >= 18:
        print("You are an adult") # output: You are an adult
    ```

## ELSE Statements
- The `else` statement is used in conjunction with if statements to execute a block of code when the condition is false.
    ```Python
    age = 15
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor") # output: You are a minor
    ```

## ELSE-IF Statements
- The `elif` statement is used to check multiple conditions after the initial if statement. It is short for "else if".
    ```Python
    score = 85
    if score >= 90:
        print("You got an A")
    elif score >= 80:
        print("You got a B") # output: You got a B
    else:
        print("You need to improve")
    ```

</details>


---
# Loops

<details>
	<summary>
	Expand
	</summary>

Loops are used to repeatedly execute a block of code. In this section, we will cover FOR loops and WHILE loops.

## FOR loops
- A FOR loop is used to iterate over a sequence (such as a list or string) or an iterable object for a specific number of times. 
    ```Python
    fruits = ["apple", "banana", "cherry"] # this is a list (more on this later)
    for fruit in fruits:
        print(fruit)
    ```
    
    <details>
        <summary>
        Output
        </summary>

    ```Shell
    apple
    banana
    cherry
    ```
    </details>
    </br>

- It can also be used to repeat an action (e.g. performing a calculation) a certain number of times. When doing this, you can use the `range( )` function which has the following syntax: `range(start [optional, default = 0], stop (required, exclusive), step [optional, default = 1])`. Note that the `stop` parameter is the only one that is required and is `exclusive` (will not execute the looping code block once the `stop` value is reached).
    - Most programming languages begin the iteration process at 0 and count up from there unless explicitly told otherwise. Thus, if you tell the loop to execute 5 times, the execution steps will be 0, 1, 2, 3, 4, which is still 5 iterations. 
    ```Python
    for i in range(5): # range(stop [exclusive])
        print(i)
    ```
    
    <details>
        <summary>
        Output
        </summary>

    ```Shell
    0
    1
    2
    3
    4
    ```
    </details>
    </br>
    
    ```Python
    for i in range(2, 6): # range(start [incl.], stop [excl.])
        print(i)
    ```
    
    <details>
        <summary>
        Output
        </summary>

    ```Shell
    2
    3
    4
    5
    ```
    </details>
    </br>
    
    ```Python
    count = 0
    for i in range(1, 10, 2): # range(start, stop, step)
        print("before: count =", count, ",  i =", i)
        count += i # += will add to, then reassign the variable (adds 1 to previous value)
        print("after:  count =", count, ",  i =", i)
    ```
    
    <details>
        <summary>
        Output
        </summary>

    ```Shell
    before: count = 0 ,  i = 1
    after:  count = 1 ,  i = 1
    before: count = 1 ,  i = 3
    after:  count = 4 ,  i = 3
    before: count = 4 ,  i = 5
    after:  count = 9 ,  i = 5
    before: count = 9 ,  i = 7
    after:  count = 16 ,  i = 7
    before: count = 16 ,  i = 9
    after:  count = 25 ,  i = 9
    ```
    </details>


## WHILE loops
- A WHILE loop is used to repeatedly execute a block of code as long as a specified condition is true.
    ```Python
    count = 0
    while count < 5:
        print(count)
        count += 1 
    ```
    <details>
        <summary>
        Output
        </summary>

    ```Shell
    0
    1
    2
    3
    4
    ```
    </details>
- Notice that the WHILE loop ended and did not execute the block of code the moment `count` was equal to 5. 

</details>


---
# Containers

<details>
	<summary>
	Expand
	</summary>

Containers are data structures used to hold multiple values. 

All built-in containers in Python have some method of "indexing" them. This means that you can retrieve an element in the container by specifying the "index" where the element resides. 

In this section, we will cover lists, tuples, dictionaries, sets, and slices.

## Lists
- Lists are a frequently used data structure in Python. Lists are ordered* collections of items that can be of different data types (even within the same list). Lists are mutable, which means their elements can be modified after being set.
    - `Ordered` means the list maintains the same data-entry order you specified when you created the list
    - You can index the list by specifying the position of the element in the list that you want to retrieve (first element starts at index 0) 
    - You can also retrieve an element by indexing backwards through the list using a negative index value. This can be useful if you expect the list size to grow in the future but you always want the last element of the list
    ```Python
    elements = [1, "a", 3, "hello", 5]
    print(elements[0])   # Output: 1
    print(elements[3])   # Output: hello
    print(elements[-2])  # Output: hello

    elements[0] = 6
    print(elements[0])   # Output: 6
    ```
    

- <details >
    <summary>
    Multi-dimensional Lists (Optional, Advanced)
    </summary>

    - Lists can also store other lists. This will create a multi-dimensional list. For example, if I want one list to hold another list, the first (outer) list stored in the variable is called a 2-dimensional list. 
    - You can think of it as `layers`. The top layer (outer list - first dimension) can hold a second layer (second dimension) of many lists. This second layer can also hold a third layer (the third dimension) of many lists, and so on.
    - An easy way to keep track is to simply count the left-most square brackets that have not been closed by a corresponding right square bracket
    - To retrieve elements from a sub-list within a list, type the variable name of the multi-dimensional outer-most list, followed by `X` number of square brackets with an index in each bracket. `X = the dimension number (layer) where the desired data resides` and the `index = the position of the sub-list (and eventually the element) containing the data`. 
        - For example let's say I have a 2D list stored in a variable called `multi_d_list`. This outer-most list contains 4 lists with 3 elements each. Working backwards, I want to obtain the last element of the last list. I can do this by typing `multi_d_list[3][2]` (remember that lists are 0-indexed). As you can see, the first square bracket refers to the desired sub-list in layer 1, and the second square bracket refers to the desired element in the chosen sub-list (these elements exist in layer 2). I can also write this as `multi_d_list[-1][-1]`, retrieving the last sub-list's last element via negative indexing.
        ```Python
        # This is a 2D list holding 1 list which holds 3 elements
        multi_d_list = [ [1,2,3] ] 
        print(multi_d_list[0][1]) # output: 2

        # This is also a 2D list which holds 3 lists of 3 elements
        multi_d_list = [ [1,2,3], [1,2,3], [4,5,6] ] 
        print(multi_d_list[2][2]) # output: 6
        ```
        ```Python
        # This is a 3D list
        # It starts getting difficult to keep track of visually 
        multi_d_list = [ [ [1,2], [3,4] ], [ [5,6], [7,8] ] ] 

        # It can also be written like this to make it easier to follow:
        multi_d_list = [            # opens the first outer list (layer 1)
            [                       # 1 of the 2 lists within the outer-most list 
                [1,2], [3,4]        # each of these 2 lists are considered the 3rd layer
            ],                      # closes first list in outer list, comma = something follows
            [                       # 2nd of 2 list within the outer-most list 
                [5,6], [7,8]        # these 2 lists are the 3rd layer of the 2nd list
            ]                       # closes the 2nd list
        ]                           # closes off the first square bracket of outer list

        print(multi_d_list[1][1][0]) # output: 7
        ```

    </details>


## Tuples
- Tuples are similar to lists, but they are immutable, meaning their elements cannot be modified once defined.
    ```Python
    immutable_tuple = (2, 3)
    print(immutable_tuple[0])  # Output: 2

    immutable_tuple[0] = 8     # Error: 'tuple' object does not support item assignment
    ```

## Dictionaries
- Dictionaries are collections of key-value pairs. Each value is associated with a unique key, allowing for fast retrieval. Dictionaries will ignore duplicate information (key-values pairs) entered.
    - You cannot refer to an element in a dictionary by index number as we have seen in previous examples.
    ```Python
    student = { 
        "name": "John",
        "age": 20,
        "grade": "A",
        "grade": "A"
    }
    print(student["age"])  # Output: 20
    print(student)         # Output: {'name': 'John', 'age': 20, 'grade': 'A'}
    ```
    - A dictionary can also be defined on a single line, but the example shown above is more legible
        - `student = {"name":"John", "age": 20, "grade": "A"}`
    - Note: Prior to Python version 3.7, dictionaries were "unordered" which meant that the values entered into the dictionary were not necessarily going to be in the same order that was specified at the time of creation. While this is not the case anymore, it is good to know as many scientific Python packages still use older version of Python.

## Sets
- Sets are unordered collections of unique elements (no duplicates). Sets are typically used for 1 of 2 purposes:
    1. If you have a lot of data and only want the unique information in the data
    1. To perform set operations such as union, intersection, and difference
    ```Python
    my_set = {1, 2, 3, 3, 3, 3, 4, 5}  # Duplicate elements are automatically removed

    print(my_set)  # Output: {1, 2, 3, 4, 5}

    # Set operations
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    union_set = set1.union(set2) # union = set1 + set2
    print(union_set)  # Output: {1, 2, 3, 4, 5}

    intersection_set = set1.intersection(set2) # inters = elements existing in both sets
    print(intersection_set)  # Output: {3}

    difference_set = set1.difference(set2)  # diff = set1 - set2
    print(difference_set)  # Output: {1, 2}
    ```    

## Slices
- Slices allow us to extract a portion (a slice) of a list, tuple, or string. We can use this to extract or copy elements of a container or string. We can even use this to modify elements of a list (tuples and strings cannot be modified because they are immutable). 
- The syntax for slicing is the same as the `range()` function discussed in the [Loops](#loops) section `(start : stop : step)`.
    ```python
    my_list = [1, 2, 3, 4, 5]

    # Extract a slice from index 1 to index 3 (exclusive)
    print(my_list[1:3])  # Output: [2, 3]

    # Copy a slice from the beginning to index 2 (exclusive)
    # Note: this will create a new list with only the chosen elements from my_list
    slice_result = my_list[:2]
    print(slice_result)  # Output: [1, 2]

    # Copy a slice from index 2 to the end (inclusive)
    slice_result = my_list[2:]
    print(slice_result)  # Output: [3, 4, 5]

    # Copy every other element from the first to the last index
    slice_result = my_list[0:5:2]
    print(slice_result)  # Output: [1, 3, 5]

    # Modify a slice from index 2 to the end (inclusive)
    my_list[2:] = ["a", "b", "c"]
    print(my_list)  # Output: [1, 2, "a", "b", "c"]

    # Also works with strings
    my_string = "Hello!"
    print(my_string[:5:2])  # Output: Hlo
    ```
- Negative indexing also works with slices.
    ```python
    # Copy a slice from 2nd last element (inclusive) to the end (inclusive) 
    slice_result = my_list[-2:]
    print(slice_result)  # Output: [4, 5]

    # Copy a slice with all the element in reverse order
    slice_result = my_list[ : : -1]
    print(slice_result)  # Output: [5, 4, 3, 2, 1]

    # Also works with strings
    my_string = "Hello! How are you?"
    print(my_string[-4:])  # Output: you?
    ```
- Slicing cannot be used on `dictionaries` because `dictionaries` cannot be indexed numerically. 
- Slicing cannot be use on `sets` because `sets` are unordered.


</details>


---
# Functions

<details>
	<summary>
	Expand
	</summary>

A function is a block of reusable code that performs a specific task. It allows you to break down your program into smaller, manageable parts.

## How to define a function
- To define a function in Python, you use the `def` keyword followed by the function name and a pair of parentheses. You can also specify parameters inside the parentheses.
    ```Python
    def greet():
        print("Hello, world!")

    greet()  # Output: Hello, world!
    ```


## Parameters and Arguments
- Parameters are placeholders in a function definition that allow you to pass values into the function. Arguments, on the other hand, are the actual values that you pass into the function when calling it.
    ```Python
    def greet(name):
        print("Hello, " + name + "!")

    greet("Alice")  # Output: Hello, Alice!
    ```


## Return statements
- The `return` statement allows a function to return a value back to the caller. It also terminates the function's execution.
    ```python
    def add(a, b):
        return a + b
        print("hello") # this will not execute

    result = add(3, 4)
    print(result)  # Output: 7
    ```

</details>


---
# Libraries

<details>
	<summary>
	Expand
	</summary>

A library is a collection of pre-written code that provides additional functionality. Python has a vast ecosystem of libraries that you can use to enhance your programs.

## How to import a library
- You can import a library in Python using the `import` keyword, followed by the library name. After importing, you can use its functions and classes.
    ```Python
    import math

    print(math.sqrt(16))  # Output: 4.0
    ```
## Examples of useful libraries: math, random, os, sys
- The `math` library provides mathematical functions and constants.
- The `random` library allows you to generate random numbers and make random choices.
- The `os` library provides functions for interacting with the operating system.
- The `sys` library provides access to system-specific parameters and functions.
    ```python
    import random

    print(random.randint(1, 10))  # Output: Random number between 1 and 10
    ```

</details>


---
# File Input and Output

<details>
	<summary>
	Expand
	</summary>

Working with files is an essential aspect of many programs. Python provides convenient ways to read data from files and write data to files. In this section, we will explore file input and output operations.

## Writing to a File
- Open the file: Use the `open()` function with the mode set to `'w'` (write mode) or `'a'` (append mode) if you want to add content to an existing file. You can use the `write()` method to write content to the file. It accepts a string as an argument. Once you finish writing, it's important to close the file using the `close()` method to ensure the changes are saved and to free up system resources.
    ```python
    file = open('output.txt', 'w')
    file.write("Hello, World!")
    file.close()
    ```
    - By default, the `'w'` mode will create a new file or overwrite the existing file with the same name. If you want to append data to an existing file, use the `'a'` mode instead.
- As it is easy to forget to close your files, which could lead to some undesirable behaviour in the code or on your computer, and to prevent having to write the close line every time, you can use a `with` statement when opening/writing files. This creates a code block which will close the files automatically for you.
    ```python
    with open('output.txt', 'w') as file:
        file.write("Hello, World!")
    ```


## Reading from a file
- You can read data from a file using the `open()` function with the appropriate file mode. The `read()` method allows you to read the contents of the file as a string. 
- The mode specifies whether you want to read, write, or append to the file. For reading, use the mode `"r"`. 
- Remember to close the file after.
    ```python
    file = open("data.txt", "r") # "r" = read only
    content = file.read() 
    print(content) # Output: the content of the data.txt file
    file.close()
    ```
- You can use a `with` statement when reading files too.
    ```python
    with open('data.txt', 'r') as file:
        content = file.read()
        print(content) # Output: the content of the data.txt file
    ```

</details>


---
# Error Handling

<details>
	<summary>
	Expand
	</summary>

In Python, an error is an exceptional event that disrupts the normal execution of a program. Errors can occur due to various reasons, such as incorrect syntax or logical mistakes. Python will often catch these errors and return a message to you.

## Types of errors
- Some common types of errors in Python include `syntax` errors, `runtime` errors, and `logical` errors. 
    - `Syntax` errors occur when the code violates the language's syntax rules. It usually indicates a typo or mistake in the code structure.
        ```python
        # Missing closing parenthesis
        print("Hello, World!"  # SyntaxError: '(' was never closed
        ```
    - `Runtime` errors, also known as exceptions, occur during the execution of the program. They are caused by invalid operations, unexpected input, or other exceptional conditions.
        ```python
        x = 10
        y = 0
        result = x / y  # ZeroDivisionError: division by zero
        ```
    - `Logical` errors occur when the code runs without any errors but produces incorrect results. These errors are often caused by mistakes in the algorithm or the program's logic.
        ```python
        radius = 5
        area = 2 * 3.14 * radius  # Incorrect formula for calculating the area of a circle
        ```

## Handling Errors with try-except Statements
- To handle errors in Python, you can use `try-except` statements. The `try` block contains the code that may raise an error, and the `except` block handles the specific error that occurs.
    ```python
    try:
        result = 10 / 0
    except Exception as e:
        print("An error occurred:", str(e)) # An error occurred: division by zero
    ```
    - The `as` keyword allows you to assign the error object to a variable (`e` in the example), which can be useful for displaying or further processing the error information.
    - The `str(e)` is performing an action known as "casting". It is casting (changing) the variable `e` to a string.
- By handling errors, you can prevent the program from abruptly terminating and provide meaningful feedback or take appropriate actions when errors occur.

</details>


---
# Object-Oriented Programming

<details>
	<summary>
	Expand
	</summary>

Object-Oriented Programming (OOP) is a programming paradigm (approach) that organizes code into objects, which are instances of classes. 

This approach focuses on creating reusable, modular, and maintainable code by representing real-world objects and their interactions. It provides a way to structure programs based on objects that have their own data (attributes) and behaviours (methods).

## Classes and Objects
- In OOP, a class is a blueprint or a template for creating objects. It defines the attributes and methods that objects of that class will have. 
- An object, also known as an instance, is created from a class and represents a specific entity.
- Example of a class:
    ```python
    class Car:
        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year

        def drive(self):
            print(f"The {self.make} {self.model} is driving.")
    ```
    - In this example, the `Car` class has attributes (`make`, `model`, `year`) and a method (`drive`). 
    - The `__init__` method is a special method, called the "constructor", which is invoked when an object is created. This means the `__init__` method will run as soon as the object is created.
    - Notice that `make`, `model`, and `year` all have `self.` as a prefix. This is Python's way of ensuring that the variables are specific to the instance of the class (when the class is created). Without `self`, the variables **could** be ambiguous and accidentally referred to or changed elsewhere in unrelated code. 
    - `self` also allows other code to call on the class-specific attributes .
    - As it stands, this class is just sitting there not doing anything because no instance of this class has been created yet (remember, it's just a blueprint).
- To create objects from a class, you can use the class name followed by parentheses, optionally passing any required arguments to the constructor.
    ```python
    car1 = Car("Toyota", "Camry", 2022)
    car2 = Car("Honda", "Accord", 2021)
    ```
    - Here, `car1` and `car2` are objects of the `Car` class, representing two different cars with their specific attributes.

## Attributes and Methods
- Attributes are the data associated with an object (variables), while methods are the functions that define the behavior of the object. They are accessed using the **dot** notation (`object.attribute` or `object.method()`).
- Example of Accessing Attributes and Calling Methods:
    ```python
    print(car1.make)  # Output: Toyota
    print(car2.year)  # Output: 2021

    car1.drive()  # Output: The Toyota Camry is driving.
    car2.drive()  # Output: The Honda Accord is driving.
    ```
    - In this example, `make` and `year` are attributes, and `drive` is a method of the `Car` objects. We access the attributes to retrieve their values and call the method to perform the associated action.

</details>

---
# THAT'S IT!!!
<details>
	<summary>
	Expand
	</summary>

While there's still a lot more to learn about Python and programming in general, this tutorial has provided you with a very strong start! 

With this knowledge, you can start coding immediately. Should you hit any roadblocks, do not get discouraged. Just about every professional programmer still has to look things up. 

</details>