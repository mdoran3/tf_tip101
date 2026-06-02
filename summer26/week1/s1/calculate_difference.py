###################################
# Problem 2: Calculate Difference #
###################################

# Write a function difference() that returns the difference between 
# two integers a and b (b should be subtracted from a).

# Example Usage: diff = difference(8, 3)
# Example Output: diff = 5

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What are we returning from the function?
#   How do we print the returned value so we can see it?

### P - Plan
# 2. Write out in plain English what you want to do: 
#     name a new variable to be returned
#     use the parameters passed in the function and subtract a from b 
#     set that equal to the new variable and return it
#
# 3. Translate each sub-problem into pseudocode:
    # func(a, b)
    #     result = a - break
    #     return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def difference(a, b):
    return a - b

a = 8
b = 3
print(difference(a,b))