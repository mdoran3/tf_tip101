############################
# PROBLEM 1: NEATLY NESTED
############################

# Given a string, return True if it is a nesting of zero or 
# more pairs of parentheses. Return False otherwise. A valid 
# pair of parentheses is defined as (). The input string will 
# only contain the characters ( or ). Your solution must be 
# recursive.

# Evaluate the time and space complexity of your solution.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we use the replace() method here?
    # Can recrusion help us slowly eliminate our string?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if the string is equal to the empty string then return True
    # if "()" cannot be found in the string, then we can return False
    # else we return a recursive call by replacing "()" with ""

# 3. Translate each sub-problem into pseudocode:
    # func(string)
        # if string == ""
            # return True
        # if "()" is not in the string:     
            # return False
        # return func(string.replace("()", "", 1))

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_nested(s):
    if s == "":
        return True
    if "()" not in s:
        return False
    return is_nested(s.replace("()", "", 1))

s = "(())"
s1 = "(())("
print(is_nested(s))
print(is_nested(s1))

#########################
# PROBLEM 2: HOW MANY 1s
#########################

# Given a sorted list of integers containing only 0s and 1s,
# count the total number of 1’s in the array in O(log n) time.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#   Can the list be empty, and if so should we return 0?
#   Are the 0s always guaranteed to come before all the 1s?

### P - Plan
# 2. Write out in plain English what you want to do:
#   Since the list is sorted, all 0s come first and all 1s come last.
#   Use binary search to find the index of the first 1 in the list.
#   If the middle element is a 1, record that index and search left for an earlier 1.
#   If the middle element is a 0, discard the left half and search right.
#   Once the first 1 is found, subtract its index from the total length to get the count of 1s.

# 3. Translate each sub-problem into pseudocode:
#   set lo = 0, hi = len(lst) - 1, first_one = len(lst)
#   while lo <= hi:
#       mid = (lo + hi) // 2
#       if lst[mid] == 1:
#           first_one = mid
#           hi = mid - 1
#       else:
#           lo = mid + 1
#   return len(lst) - first_one

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_ones(lst):
    lo, hi = 0, len(lst) - 1
    first_one = len(lst)  # default: no 1s found
    while lo <= hi:
        mid = (lo + hi) // 2
        if lst[mid] == 1:
            first_one = mid
            hi = mid - 1  # keep searching left for earlier 1
        else:
            lo = mid + 1
    return len(lst) - first_one
			
test_lst = [0, 0, 0, 0, 1, 1, 1]
print(count_ones(test_lst))
test_lst2 = [0, 0, 0, 0, 1, 1, 1, 1, 1]
print(count_ones(test_lst2))
test_lst3 = [0, 0, 0, 1, 1, 1, 1, 1, 1]
print(count_ones(test_lst3))

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
#   Can the array have 0 rotations (i.e., already sorted)?
#   Are all elements unique?

### P - Plan
# 2. Write out in plain English what you want to do:
#   The number of rotations equals the index of the minimum element.
#   Use binary search: if the middle element is greater than the rightmost,
#   the minimum is in the right half; otherwise it's in the left half.

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

###########################
# PROBLEM 5: MERGE SORT 1
###########################

# Merge sort is a sorting algorithm that takes in an 
# unsorted list and returns a sorted list in O(n log n) 
# time which is faster than many other sorting algorithms 
# that have O(n²) time complexity. It uses a divide and 
#             conquer approach.

# Merge sort works by using a divide and conquer approach: 
# it divides the array into two halves until each sublist 
# contains only a single element, then it recursively sorts 
# each sublist, and merges the sorted sublists into a sorted 
# array.

# Given the pseudo-code and helper function merge() below, 
# implement the merge_sort() function.


### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#   Can the input list be empty, and if so should we return an empty list?
#   Does the function need to sort in-place or return a new sorted list?

### P - Plan
# 2. Write out in plain English what you want to do:
#   If the list has 0 or 1 elements, it is already sorted — return it as is.
#   Otherwise, split the list in half, recursively sort each half,
#   then merge the two sorted halves back together using the merge() helper.

# 3. Translate each sub-problem into pseudocode:
#   def merge_sort(lst):
#       if len(lst) <= 1: return lst
#       mid = len(lst) // 2
#       left = merge_sort(lst[:mid])
#       right = merge_sort(lst[mid:])
#       return merge(left, right)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# Helper function: Merges two sorted lists into one sorted list
def merge(left, right):
    result = [] # List to store the merged result
    i = j = 0 # Pointers to iterate over left and right input arrays

    # Compare elements from left and right halves of the list and add them to the
    # result list in the correct order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


lst = [5,3,4,2,1]
print(merge_sort(lst))