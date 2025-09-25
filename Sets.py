#Set items are unchangeable, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Sets cannot have two items with the same value.
#Note: The values True and 1, False and 0 are considered the same value in sets, and are treated as duplicates


#A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}
print(set1)


'''There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''

#2 Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if "banana" is present in the set

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#To add one item to a set use the add() method.
thisset.add("orange")

print(thisset)

#To remove an item in a set, use the remove(), or the discard() method.
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

'''There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.'''

#union() method returns a new set with all items from both sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#You can use the | operator instead of the union() method, and you will get the same result.

#The update() method inserts the items in set2 into set1

#The intersection() method will return a new set, that only contains the items that are present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set

'''Python frozenset
frozenset is an immutable version of a set.

Like sets, it contains unique, unordered, unchangeable elements.

Unlike sets, elements cannot be added or removed from a frozenset.'''
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))