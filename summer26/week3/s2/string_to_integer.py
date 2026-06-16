################################
# Problem 1: String to Integer #
################################

'''
Write a function string_to_integer_mapping() that takes 
in a string of digits s as a parameter and returns a list 
where each element is the integer value of the corresponding 
digit in the string.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is casting and how is it down in Python?
#   What is the time and the space complexity of this algorithm?

### P - Plan
#   create an empty list
#   iterate through the string 
#   cast each char to an int and append it to the list
#   return the list

# 3. Translate each sub-problem into pseudocode:
#   func(str):
#       nums = []
#       for char in str:
#           new_int = int(char)
#           append new_int to nums
#       return nums

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def string_to_integer_mapping(s):
    nums = []
    for char in s:
        nums.append(int(char))
    return nums

# Example Input: s="12345"
# Example Output: [1, 2, 3, 4, 5]

s="12345"
print(string_to_integer_mapping(s))