# for loops
print("----- e.g. FOR loop 1 -----")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("\n----- e.g. FOR loop 2 -----")
for i in range(5): # range(stop)
    print(i)

print("\n----- e.g. FOR loop 3 -----")
for i in range(2, 6): # range(start, stop)
    print(i)

print("\n----- e.g. FOR loop 4 -----")
count = 0
for i in range(1, 10, 2): # range(start, stop, step)
    print("before: count =", count, ",  i =", i)
    count += i
    print("after:  count =", count, ",  i =", i)



# while loops
print("\n----- WHILE loop -----")
count = 0
while count < 5:
    print(count)
    count += 1
