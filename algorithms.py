#Algorithm is a set of instructions that is done in a sequence to solve a problem. 

###
#Say you want to create an algo to dtermine how many food roder tickets are in the queue to the kitchen.

# write it in pseudocode first
###

#Let T = 0
#for each ticket on rail
#   Set T = T + 1
#Return T

#This pseudocode above starsts at 0 and then checks to see how many tickets are on the rail.
#If a ticket is found it will then increase the counter by 1.
#And finally, it will return the total count

#One aspect of algo writing is how efficient it is. This is called optimization
#how to get the answer faster
#In the real world, I could count by 2 instead by 1 at a time. How do I write this in pseudocode

#let T = 0
#for each pair of tickets on the rail
#   Set T = T + 2

#the code above doesn't cover all usecases

#What if there are 3 orders on the rail?

#need to fix the code by adding a condition to handle this edge case
#let T = 0
#
#    for each pair of ticket on rail
#        Set T = T + 2
#    
#    if 1 ticket remains then
#        Set T = T + 1
#    
#    Return T