# Lists
print("----- Lists -----")
elements = [1, "a", 3, "hello", 5]
print(elements[0])  # Output: 1
print(elements[3])  # Output: hello
print(elements[-2])  # Output: hello
elements[0] = 6
print(elements[0])  # Output: 6

print("----- Multidimensional Lists -----")
multi_d_list = [ [1,2,3] ] # this is a 2D list
print(multi_d_list[0][1]) # output: 2
multi_d_list = [ [1,2,3], [1,2,3], [4,5,6] ] # this is also a 2D list
print(multi_d_list[2][2]) # output: 6
multi_d_list = [ [ [1,2], [3,4] ],  [ [5,6], [7,8] ] ] # this is a 3D list
multi_d_list = [    # opens the first outer list (layer 1)
    [   # 1 of the 2 lists within the outer-most list 
        [1,2], [3,4]    # each of these 2 lists are considered the 3rd layer
    ],    # closes first list in outer-most list, comma means something follows
    [     # 2nd of 2 list within the outer-most list 
        [5,6], [7,8]    # these 2 lists are the 3rd layer of the 2nd list
    ]   # closes the 2nd list
]    # this closes off the first square bracket of the outer-most list
print(multi_d_list[1][1][0]) # output: 7


# Tuples
print("\n----- Tuples -----")
immutable_tuple = (2, 3)
print(immutable_tuple[0])  # Output: 2
try: # don't worry about try-except right now. This will be described later
    immutable_tuple[0] = 8 # can't change
except Exception as exec: # just printing the error and continuing execution
    print("Error:",exec)


# Dictionaries
print("\n----- Dictionaries -----")
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "grade": "A"
}
print(student["age"])  # Output: 20
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'A'}


# Sets
print("\n----- Sets -----")
my_set = {1, 2, 3, 3, 3, 3, 4, 5}  # Duplicate elements are automatically removed
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2) # union = set1 + set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
intersection_set = set1.intersection(set2) # inters = elements existing in both sets
print(intersection_set)  # Output: {3}
difference_set = set1.difference(set2) # diff = set1 - set2
print(difference_set)  # Output: {1, 2}


# Slicing
print("\n----- Slicing -----")
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

# Also works with strings
my_string = "Hello!"
print(my_string[:5:2])  # Output: Hlo

# Copy a slice from 2nd last element (inclusive) to the end (inclusive) 
slice_result = my_list[-2:]
print(slice_result)  # Output: [4, 5]

# Copy a slice with all the element in reverse order
slice_result = my_list[ : : -1]
print(slice_result)  # Output: [5, 4, 3, 2 , 1]

# Modify a slice from index 2 to the end (inclusive)
my_list[2:] = ["a", "b", "c"]
print(my_list)  # Output: [1, 2, "a", "b", "c"]
