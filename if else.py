# Python - Conditions and If statements
# Python supports usual logical conditions:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions are used in if statements and loops.

# Basic if statement
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Indentation
# Python uses indentation instead of curly braces.
# Wrong indentation will raise an error:
a = 33
b = 200
if b > a:
 print("b is greater than a")  # ERROR

 # Elif
# "elif" means "else if" - check another condition if the first is False
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
# "else" catches anything not caught by previous conditions
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# else without elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If
a = 200
b = 33
if a > b: print("a is greater than b")

# Short Hand If ... Else (Ternary Operator)
a = 2
b = 330
print("A") if a > b else print("B")

# Multiple conditions in one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Logical Operators

# AND - both conditions must be True
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# OR - at least one condition is True
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# NOT - reverse the result
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested If
# if statements inside if statements
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# if statements cannot be empty
# use "pass" to avoid an error

a = 33
b = 200
if b > a:
    pass

