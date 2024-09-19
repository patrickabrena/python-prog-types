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
#print(global_list)
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

#print(add_to_list([5, 6, 7], 8))

#pros for pure functions
# - Known outcome
# - Consistent and reliable
# - ability to cache
# - multi-threaded programs(more than one process can run concurenttly)

#how to alter a normal function to a pure function
#my_list = [1, 2, 3]
#
#def add_to_list1(item):
#    return my_list.append(item)
#
#add_to_list1(4)
#print(my_list)

#this example above is not a pure functions because the data has been altered on the global scope

my_list = [1, 2, 3]

def add_to_list_pure(a_list, num):
    a_list.append(num)
    return a_list

new_list = add_to_list_pure(my_list, 5)

#print(my_list) # my_list is still modified so not a pure function
#print(new_list)

#refer to function above that uses copy() to keep original list unmodified


#searching through a file system is where recursion is present
#what is recursion, a function that calls itself

#going to see both for loop and recursive solution to finding the factorial of a number


#LOOPING SOLUTION
def find_factorial_by_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial

print(find_factorial_by_looping(5))


#RECURSIVE SOLUTION
def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)
    
print(find_factorial_recursive(5))

#How the recursive solution is working....
#find_factorial_recursive(5)
# 5 * factorial(4)
# 5 * (4 * factorial(3)) ....

# 5 * (4 * (3 * (2 * (1 * factorial(0)))))
# 5 * (4 * (3 * (2 * (1 * 1))))

#recursion example with tower of hanoi
#objective is to move "n" number of disks from one tower to another following a set of rules. 
#   - Only one disk can be moved at a time
#   - Only the upper disk of any of the towers can be moved
#   - Larger disks cannot be placed over small disks

#Optimal scenario of solving the puzzle, the total moves will be 2^n-1 where "n" is number of disks

#Can break this problem down in 3 main code blocks,
#   1st section covers the base condition to make sure the function stops calling itself to stop an infinite loop
#   2nd section covers the actual recursive call to keep calling the function
#   3rd section is the driver code (actual call to the function or class) that consists of the tower names you pass as arguemnts to the functions, along with the number of disks.

# RECURSIVE FUNCTION FOR TOWER OF HANOI
def hanoi(disks, source, helper, destination):
    #Base Condition
    if (disks == 1):
        print("Disk {} moves from tower {} to tower {}".format(disks, source, helper, destination))
        return
    
    #recursive calls in which the function calls itself
    hanoi(disks - 1, source, destination, helper)
    print("Disk {} moves from tower {} to tower {}".format(disks, source, helper, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver COde
disks = int(input("Number of disks to be displaced: "))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
#actual function call
hanoi(disks, "A", "B", "C")
#notice that it takes 2^3 - 1 = 7 outputs


