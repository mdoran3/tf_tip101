#############################
# Problem 2: Delete Minimum #
#############################

'''
Write a function delete_minimum_elements(nums) 
that takes in a list of integers nums as a parameter 
and continuously removes the minimum element until 
the list is empty. The function returns a new list 
of all the elements in nums in the order in which 
they were removed.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How will a while loop help us in this problem?
#   How do we initialize the minimum value and why?

### P - Plan
#   create an empty list
#   use a while loop to continute while the nums parameter is not empty
#   use a for loop to iterate through each element and find min on each iteration
#   append each min to the empty list created
#   return that list that was created

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       mins = []
#       while nums:
#           for num in nums:
#               if num < min:
#                   min = num
#           i = nums.index(min)
#           popped = nums.pop(i)
#           mins.append(popped)
#       return mins

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def delete_minimum_elements(nums):
    mins = []
    while nums:
        min = float('inf')
        for num in nums:
            if num < min:
                min = num
        i = nums.index(min)
        popped_min = nums.pop(i)
        mins.append(popped_min)
    return mins

# Simple version Co-authored by Claude AI
def delete_minimum_elements_v2(nums):
    mins = []
    while nums:
        minimum = min(nums)
        nums.remove(minimum)
        mins.append(minimum)
    return mins

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements_v2(nums)
print(removed_lst)

# Example Output: [1,2,3,3,5,8]