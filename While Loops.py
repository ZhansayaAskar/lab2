# Python - While Loops
# Python has two primitive loop commands:
# 1) while loops
# 2) for loops


# The while Loop
# Execute a set of statements as long as a condition is true
i = 1
while i < 6:
    print(i)
    i += 1
# Note: remember to increment i, otherwise the loop will run forever


# The break Statement
# Stop the loop even if the while condition is still true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# The continue Statement
# Stop the current iteration and continue with the next
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# The else Statement
# Run a block of code once when the condition is no longer true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
