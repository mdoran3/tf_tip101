# PROBLEM 1: LONG PRESSED

# Write a function is_long_pressed() that takes in a string name 
# and a string typed as parameters. Imagine your friend is typing 
# their name into a keyboard and when typing a character, the key 
# might get long pressed and the character will be typed 1 or more 
# times.

# The function should examine the typed characters and return True 
# if it is possible that it was your friends name with some characters 
# being long pressed and False otherwise.

# Use the two-pointer approach to solve the problem, which is a 
# common technique in which we initialize two variables (also called 
# a pointer in this context) to track different indices or places in 
# a list or string, then moves the pointers to point at new indices 
# based on certain conditions. A common variation of this technique 
# is to point one variable at the beginning of one string and a second 
# pointer at the beginning of a second string, then increment each 
# pointer conditionally to solve a problem.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What condition will make this function return False?
    # Are there any other conditions that will make it False?
    # When should pointers be moved?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Declare to pointers - one for name and one for typed
    # If name equals typed, return True since equal strings are True under the givens
    # Create a while loop and continue until the name pointer is higher than length of name 
        # same logic for type (use AND logic)
    # If name as repeasted chars but typed does not, we automatically return False
    # Else we keep moving forward and update the pointers as follows:
        # if name[i] == name [i-1] then pointer 1 goes up by 2 indices while pointer 2 goes up by 1
        # If typed[i] == typed[i-1] then pointer 2 goes up by 2 indices while pointer1 goes up by one
        # else just increment pointer 1 and pointe 2 each by 1
    # return True outside of the while loop

# 3. Translate each sub-problem into pseudocode:
    # pointer1 = 1
    # pointer2 = 1
    # if name equals type: {return True}
    # while pointer1 <= length of name AND pointer2 <= length of typed
        # if name at pointer1 EQUALS name at pointer1 -1 AND typed at pointer2 NOT EQUAL to typed at pointer2 -1:
            # {return False}
        #elif name at pointer1 EQUALS name at pointer1 -1
            # pointer1 += 2
            # pointer2 += 1
        #elif typed at pointer2 EQUALS typed at pointer2 -1
            # pointer1 += 1
            # pointer2 += 2
        #else
            # pointer1 += 1
            # pointer2 += 1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_long_pressed(name, typed):
    p1 = 1
    p2 = 1

    if name == typed:
        return True

    while p1 <= len(name)-1 and p2 <= len(typed)-1:
        if name[p1] == name[p1-1] and typed[p2] != typed[p2-1]:
            return False
        elif name[p1] == name[p1-1]:
            p1 += 2
            p2 += 1
        elif typed[p2] == typed[p2-1]:
            p1 += 1
            p2 += 2
        else:
            p1 += 1
            p2 += 1
    return True
    
name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

# PROBLEM 2: SHARING COOKIES

# Imagine you're an awesome babysitter and want to give the kids you're 
# looking after some cookies as a snack.
# Each child i has a greed factor g[i], which is the minimum size of a 
# cookie that the child will be content with.
# Each cookie j has a cookie size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the 
# child will be content.
# If s[j] < g[i], the child will not be content.

# Write a function find_content_children() that takes in the greed list
# g and the cookie size list s as parameters and maximizes the number of 
# content children you are babysitting! The function returns

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Which array gives us the quantity of children?
    # What if the satisfied array is bigger than the greed array?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set 3 variables for children, count of satisfied children, and position
    # Make a while loop for while there are still children left to check if they are satisfied
        # if the 0th position of the s array is greater than or equal to the 0th position of the g array, 
            # then count gets incremented by 1
        # increment position by 1
        # increment children by 1
    # return count

# 3. Translate each sub-problem into pseudocode:
    # children, count, pos = 0
    # while children < length of g
        # if s[pos] >= g[pos]
            # increment count by 1
        # increment pos by 1
        # increment children by 1
    # return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_content_children(s, g):
    children = 0
    count = 0
    pos = 0
    while children < len(g):
        if s[pos] >= g[pos]:
            count += 1
        pos += 1
        children += 1
    return count

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

print(find_content_children(s, g))
# Output: 2 

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

print(find_content_children(s, g))
# Output: 2 
