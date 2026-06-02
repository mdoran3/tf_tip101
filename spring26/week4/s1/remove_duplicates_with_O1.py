# Write a function remove_duplicates() that takes in a sorted list of 
# integers nums as a parameter and removes the duplicates in-place such 
# that each element appears only once. Do not allocate extra space for 
# another array; you must do this by modifying the input list with O(1) 
# extra memory. The function returns the new length of the list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is a helpful pytong function we can use to remove an element?
    # Can we use two pointers? Where might we point them?

### P - Plan
# 2. Write out in plain English what you want to do: 

# 3. Translate each sub-problem into pseudocode:

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def remove_duplicates(nums):
    pos = 1
    while pos < len(nums):
        if nums[pos] == nums[pos-1]:
            del nums[pos]
        else: 
            pos += 1
    return len(nums)

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list