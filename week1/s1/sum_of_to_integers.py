def sum(a, b):
    return a + b

first_sum = sum(13, 27)

print(sum(first_sum, first_sum))

# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
  # How many parameters does the function take? 
  # What data types are the params?
  # Do we have any constraints (things we cannot use)?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a function that takes to int params
    # return the sum of the two params
    # create a variable that calls this function with the given integers
    # now pass this created variable in as both the params back into sum again to double the sum
# 3. Translate each sub-problem into pseudocode:
    #func(var1, var2) - two params
    #   return var1 + var2
    # first_sum = func(var1, var2)
    # print func(first_sum, first_sum)
  


### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sum(a, b):
    return a + b

first_sum = sum(13, 27)

print(sum(first_sum, first_sum))