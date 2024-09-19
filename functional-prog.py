#custom function
coffees = ['Espresso', 'Latte', 'Cappuccino', 'Macchiato', 'Americano', 'Decaf',]

def reverse(str):
    return str[::-1] # learn more on this later (slice function)

reversed_coffees = map(reverse, coffees)

for x in reversed_coffees:
    #print(x)
    pass



# Difference between traditional and pure functions
#Pure funcs have no effect beyond its own scope
#   -ex. if there is a list made on the global scope, it can't add something to that list or alter it in any way.

#Determine whether the funtion below is pure or not

#global scope
global_list = [1, 2, 3]

def add_to(item):
    return global_list.append(item)
add_to(4)
print(global_list)
#output is [1, 2, 3, 4]

#it's NOT a pure function because it changes the global_list by appending the item which is passed as an argument

#to make this a pure function you need to think abt how to extend the function to ACCEPT a list as an argument,
#add the item to the list WITHOUT modifying the original list, 
#and how to retun a new list with the newly added item.
#solution is to create a new list and copy or clone the data from the original list. 

def add_to_list(lst, item):

    n1 = lst.copy()
    n1.append(item)
    return n1

print(add_to_list([5, 6, 7], 8))
