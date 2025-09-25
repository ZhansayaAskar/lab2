# Python - For Loops
# A for loop is used for iterating over a sequence (list, tuple, set, dictionary, string).
# It executes a block of code once for each item in the sequence.

# Example: loop through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Looping Through a String
for x in "banana":
    print(x)


# The break Statement
# Stop the loop before it has looped through all items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Break before print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# The continue Statement
# Skip the current iteration and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


# The range() Function
# range() generates a sequence of numbers
for x in range(6):
    print(x)   # 0 to 5

for x in range(2, 6):
    print(x)  # 2 to 5

for x in range(2, 30, 3):
    print(x)   # 2, 5, 8, ...


# Else in For Loop
# The else block runs when the loop finishes normally (no break)
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Example with break (else does not run)
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


# Nested Loops
# Loop inside a loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)


# The pass Statement
# For loops cannot be empty
for x in [0, 1, 2]:
    pass
