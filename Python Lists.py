thislist = ["apple", "banana", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function
print(len(thislist))

#List items can be of any data type
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
#There are four collection data types in the Python programming language:

'''List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.'''

#2 Access Items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#3 Change Item Value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist[1:3] = ["watermelon"]
print(thislist)

#4 Append Items

#To add an item to the end of the list, use the append() method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#The insert() method inserts an item at the specified index
thislist.insert(1, "kiwi")
print(thislist)

#To append elements from another list to the current list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#5 Remove List Items
#The remove() method removes the specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index.
thislist.pop(1)
print(thislist)
#The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#del thislist  delete the list completely

#The clear() method empties the list.The list still remains, but it has no content.

#6 Loops
#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#7
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The condition is like a filter that only accepts the items that evaluate to True
newlist = [x for x in fruits if x != "apple"]

#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]

#Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]

#8 
#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#8 join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

'''Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
      