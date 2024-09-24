#comprehensions in python are a way to create a new sequence from an already existing sequence

# 4 main types of comprehensions in Python
#   List comprehension
#   Dictionary comprehension
#   Set comprehension
#   Generator comprehension

#LIST COMPREHENSION

#syntax is [ <expression> for x in <sequence> if <condition>] 

data = [2,3,5,7,11,13,17,19,23,29,31]

#Ex1: List comprehension: updating the SAME list
data = [x * 2 for x in data]
#print("Updating the list: {}".format(data))

#Ex2: List comprehension: creating a DIFFERENT list with the updated values from EX 1
new_data = [x * 2 for x in data]
#print("Creating new list: {}".format(new_data))

#Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0]
#print("Divisible by 4: {}".format(fourx))

#Ex4: Althernatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0]
#print(fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
#print("Nines: ", nines)

#DICTIONARY COMPREHENSIONS

#syntax for dictionary comprehension is:

#dict = {key:value for key, value in <sequence> if <condition>}

#Dcitionary comprehensions takes on or two lists as input and creates a dictionary out of it. 
#Examples of dict comps using one list and two lists

#Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range*(): {}".format(usingrange))

#Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July"]
number = [1, 2, 3, 4, 5, 6, 7, 8, 9,] # notice

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

#Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#Set comprehension
#The set comprehension deals with the SET data type and is very similar to list comprehension.
#Only key difference is the use of curly brackets for sets instead of square brackets in lists.

set_a = {x for x in range(10,20) if x not in [12, 14, 16]}
print(set_a)

#Generator Comprehension

#Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets.
#They are also more memory efficient as compared to list comprehensions.
data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")

#code above creates a generator object of the class generator instead of a list. 
#The elements in this iterator object cannot be directly accessed and need help with for loops

z = ["alpha","bravo","charlie"]
new_z = [i[0]*2 for i in z]
print(new_z)