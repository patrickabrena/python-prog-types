menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

#going to filter the list by printing all the coffees that start with letter "C"

#covering the map function
def find_coffee(coffee):
    if coffee[0] == "c":
        return coffee


#map_coffee = map(find_coffee, menu)
#print(map_coffee) returns map object
#for x in map_coffee:
#    print(x)

#going to show output with filter now

filter_coffee = filter(find_coffee, menu)
print(filter_coffee) # returns filter object
#iterate through filter object
for x in filter_coffee:
    print(x)



#MAIN DIFFERENCE IN MAP AND FILTER
# MAP takes all objects in the list and allows you to apply a function to it
# FILTER does the same with an extra step of creatinga  new list and only returns vals where the evaluated functions return true