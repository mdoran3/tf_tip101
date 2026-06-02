#############################
# PROBLEM 4: COUNT ROTATIONS
#############################

# You are given a circularly sorted list of integers. A circularly sorted 
# list of integers is a sorted list whose elements have then been rotated 
# some number of times such that the last element of the array becomes the 
# first element of the array. Write a function count_rotations() that returns 
# the total number of times the array is rotated. Assume there are no 
# duplicates in the array.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# - Can the array have 0 rotations (i.e., already sorted)?
# - Are all elements unique?

### P - Plan
# 2. Write out in plain English what you want to do:
# The number of rotations equals the index of the minimum element.
# Use binary search: if the middle element is greater than the rightmost,
# the minimum is in the right half; otherwise it's in the left half.

# 3. Translate each sub-problem into pseudocode:
# left = 0, right = len(nums) - 1
# while left < right:
#     mid = (left + right) // 2
#     if nums[mid] > nums[right]: left = mid + 1
#     else: right = mid
# return left  # index of minimum = number of rotations

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_rotations(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left

nums = [8, 9, 10, 2, 5, 6]
print(count_rotations(nums))