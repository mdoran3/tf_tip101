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
