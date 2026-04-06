###########################
# PROBLEM 3: BINARY SEARCH
###########################

# Thus far, we've mostly been using an iterative implementation
# of the binary search algorithm. Recursive implementations of
# binary search are also very common. Implement binary_search()
# recursively.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#   Should the function return the index of the target in the original array,
#       or just whether the target exists?
#   Can we assume the input array is always sorted?

### P - Plan
# 2. Write out in plain English what you want to do:
#   Find the middle element of the current array. 
#   If it equals the target, return its index. 
#   If the target is greater, recursively search the right half. 
#   If the target is smaller, recursively search the left half. 
#   If the array is empty, return -1 (target not found).

# 3. Translate each sub-problem into pseudocode:
#    def binary_search(nums, target):
#        base case: if nums is empty, return -1
#        mid = len(nums) // 2
#        if nums[mid] == target: return mid
#        elif nums[mid] < target:
#            result = binary_search(right half)
#            return -1 if not found, else mid + 1 + result (adjust index offset)
#        else:
#            return binary_search(left half)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def binary_search(nums, target):
    if not nums:
        return -1
    mid = len(nums) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        result = binary_search(nums[mid+1:], target)
        return -1 if result == -1 else mid + 1 + result
    else:
        return binary_search(nums[:mid], target)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(binary_search(nums, target))
