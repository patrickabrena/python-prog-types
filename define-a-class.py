#Learning Objectives

#Create classes and objects with help of examples.
#Lets look at the basic members of a class.
#These can be the attributes or the data members, the methods, and additionally the comments that you can include.
#These members can be shown with the help of an example below.
#Imagine you want to make a class of some house. 
#You begin by creating a class for it

#Ex 1
class House:
    '''
    This is a stub for a class representing a house that can be sued to create objects
    and evaluate different metrics that we may require in constructing it
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calcualte the costs from the area of the house

# code above starts with multiline comment, can be called a docstring
# next line is the class definition class House:
# followed by a couple data members or ATTRIBUTES: num_rooms and bathrooms
# This is then followed by a function definition with pass keyowrd to tell python to continue execution without error

# Code is completely defines the class and fucntions present inside it, but not useful unless you call or instantiate it

# Instantiate House class with "house" as the instance or object
house_a = House()
print(f"Attribute access through instantiation: {house_a.num_rooms}")
print(f"Attribute access through direct call: {House.num_rooms}")

#you can update the num_rooms variable called on house object to 7
house_a.num_rooms = 7
print(f"Attribute access through instantiation: {house_a.num_rooms}")
print(f"Attribute access through direct call: {House.num_rooms}")
#In the code above, an instance of a class House: is created and then num_rooms attribute is modified for that instance with a value of 7
#Updates the instance attribute but not the class attribute

#This time instead of an instance attribute, you will modify the class attribute by directly calling it over the class as follows:
House.num_rooms = 7
print(f"Attribute access through instantiation: {house_a.num_rooms}")
print(f"Attribute access through direct call: {House.num_rooms}")


#REVIEW THIS!!!!
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost



house = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)