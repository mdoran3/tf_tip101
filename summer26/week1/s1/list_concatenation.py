#################################
# Problem 3: List Concatenation #
#################################

# Given an integer list nums of length n, create a function 
# concatenate_list() that creates and returns a list ans of 
# length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
# for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums lists.

# Example Input: [1,2,3,4]
# Example Output: [1,2,3,4,1,2,3,4]

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is concatenation?
#   What does is mean for a list to be concatenated?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   create a new list variable
#   add the parameter to itself with the "+" mathematical operator and set it equal to var
#   return the var

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       new_list = nums + nums
# return new_list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def concatenate_list(nums):
    lst = nums + nums
    return lst

nums = [1,2,3,4]
print(concatenate_list(nums))