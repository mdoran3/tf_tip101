##############################
# Problem 6: Below Threshold #
##############################

# Write a function count_less_than() that takes in a 
# list of integers numbers and an integer threshold as 
# parameters and returns the number of items in numbers 
# that are less than threshold.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How many times do we need to iterate through this list?
#   What would the asymptotic time complexity be of this algorithm?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   create a variable that tracks the count or frequency
#   iterate through the list
#   check each number and see if it less than threshold
#   if it is less than threshold, add it to count

# 3. Translate each sub-problem into pseudocode:
#   func(numbers, threshold)
#       for num in numbers
#           if num < threshold
#               count ++  
#       return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count += 1
    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)