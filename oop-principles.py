#OOP principles

#4 main pillars of OOP
#   - encapsulation
#   - polymorphism 
#   - inheritance
#   - abstraction

#ENCAPSULATION is having methods and variables bound within a given unit.
#this unit in python is called a class
#these concepts are better understood with scope, such as global scope and local scope

#EXAMPLE - Little Lemon company may have different departments like...
#   - Inventory
#   - Marketing
#   - Accounts
#May be required to deal with data and operations for each of them separately. 
#Classes and objects help in encapsulation and in turn restrict the different functionalities

#Encapsulation also used for hiding data and its internal representation
#Acess modifiers represented by keyowrds like PUBLIC, PRIVATE and PROTECTED are used for info hiding. 
#The use of single and double underscores for this purpose in Python is a substitute or this practice.

#Example of protected members in Python
class Alpha:

    def __init__(self):
        self._a = 2. #Proteccted member "a"
        self.__b = 2. # Private member "b"

#self._a is a protected member and can be accessed by the class and its subclass

#Private members in Python are conventionally used with preceding double underscores:__. self.__b is a private member of teh class Alpha and can only be accessed from within the calss Alpha.

#NOTE: these private and proteected members can still be accessed from outside of the class by using public methods to access them
# THIS IS CALLED NAME MANGLING
# name mangling is the use fo two leading underscores and one trailing underscore, for example: _class__identifier where class is the name of the class and identifier is the data member that I want to access


#POLYMORPHISM
# this is something can have many forms.
# Everything in Python gis inherently an object, 
# so polymorphism in python, it can be an operator, method or any object of some class.
# examples of polymorpism using built-in functions and operations

string = "poly"
num = 7
sequence = [1,2,3]
new_str = string * 3
new_num = 7 * 3
new_sequence = sequence * 3

print(new_str, new_num, new_sequence)


#INHERITANCE
#more of it covered later


#class Parent:
#   Members of the parent class
#
#class Child(Parent):
#   Inherited members from parent class
#   Additional members of the child class


#ABSTRACTION

#Means for both hiding important info aswell as unnecessary info in a block of code.

#from abc import ABC,   
#class ClassName(ABC):
#    pass