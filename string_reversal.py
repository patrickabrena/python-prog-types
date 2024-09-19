#Reversing a string

#showing slice function first

# str[stasrt:stop:step] this is called extended slice sytax

#the start and stop parameters are the indicies between which the function manipulates the string

trial = "reversal"

new_trial = trial[::-1] # leave the first two params empty by doing :: This instructs python to use the entire string

# the -1 indicates that the string needs to be traversed from the right, 1 index position at a time
print("slice method solution: {}".format(new_trial))


#Using recursion to reverse the string
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0] # string traversed from the front, skippuing the first character in every loop and the first character skipped is appended to remaining string
    
str = "reversal"

reverse = string_reverse(str)
print("recursive solution: {}".format(reverse))