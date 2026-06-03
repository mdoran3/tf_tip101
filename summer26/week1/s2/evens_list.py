#########################
# Problem 7: Evens List #
#########################

# Write a function get_evens() that takes in a list 
# of integers lst as a parameter and returns a list 
# of all even numbers in the list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is the space complexity of this algorithm and why?
#   What key mathematical feature, often used in CS, whill be utilized 
#       in this problem for find evens?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   Create an evens list variable
#   Iterate through the lst
#   Check if each number in list is even
#   If it is even, add it to the evens list
#   return evens list

# 3. Translate each sub-problem into pseudocode:
#   func(lst):
#       evens = []
#       for num in lst:
#           if num is even
#               append to evens
#       return evens

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def get_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)