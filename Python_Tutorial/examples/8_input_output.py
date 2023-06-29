# Write
with open('output.txt', 'w') as file:
    file.write("Hello, World!")


# Read
with open('output.txt', 'r') as file:
    content = file.read()
    print(content) # Output: the content of the data.txt file
