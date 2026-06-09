##############################
# Problem 8: Index-Value Map #
##############################

# Write a function index_to_value_map() that takes in a 
# list lst and returns a dictionary that maps the index 
# of each element in lst to its value.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How does the enumerate feature work in Python?
#   How do I add the key and value to a function in Python?

### P - Plan
#   create an empty dict
#   iterate through list and enumerate
#   add key,value pair to empty dict
#   return dict

# 3. Translate each sub-problem into pseudocode:
#   func(lst):
#       enumerated_dict = {}
#       for index, item in enumerate(lst):
#           add key,value to enumerate_dict{}
#       return enumerated_dict

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def index_to_value_map(lst):
    fruits = {}
    for i, item in enumerate(lst):
        fruits[i] = item
    return fruits

# Example Input:
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))

# Example Output: {0: "apple", 1: "banana", 2: "cherry"}