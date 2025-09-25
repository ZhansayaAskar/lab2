#1 we use the + operator to add together two values
print(10 + 5)

'''Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
#Arithmetic Operators
x = 5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Assignment Operators
x = 5
print(x)

x += 3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

x %= 3
print(x)

x //= 3
print(x)

x **= 3
print(x)

x = 5
x &= 3
print(x)

x |= 3
print(x)

x ^= 3
print(x)

x = 8
x >>= 3
print(x)

x <<= 3
print(x)

print(x := 3)
print(x)

#Comparison Operators
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical Operators

print(x < 5 and x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))

#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Bitwise Operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~6)
print(6 << 2)
print(6 >> 2)
