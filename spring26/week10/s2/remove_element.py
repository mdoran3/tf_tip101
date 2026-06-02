#############################
# PROBLEM 2: REMOVE ELEMENT #
#############################

# Given a list of integers nums and an integer val, remove all 
# occurrences of val in nums in-place. The order of the elements 
# may be changed. Then return the number of elements in nums which 
# are not equal to val.

# Consider the number of elements in nums which are not equal to 
# val be k, for your response to be acceptable, you need to do the 
# following things:

# Change the list nums such that the first k elements of nums contain 
# the elements which are not equal to val. The remaining elements of 
# nums are not important as well as the size of nums.
# Return k

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Since the nums will be changing its size, how can we iterate and keep track of where we are?
    # How can the .pop() function help yes here?
    # if we are properly popping elements, can we just return the length of the modified list?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a length function for the length of nums
    # initialize an i variable to 0
    # iterate through numer while length is > 0 (make sure to be decrementing this)
    # if the current iteration index in nums is equal to the target val, then pop this index from nums
    # Make sure to decrementh length here!
    # Else, increment "i" variable and decrement length as well
    # return the length of the nums list

# 3. Translate each sub-problem into pseudocode:
    # create a length variable set to the length of nums
    # initialize i to 0
    # iterate while length is greater than 0
    #     if the current element at i equals val, pop it from nums and decrement length
    #     otherwise, increment i and decrement length
    # return the length of nums

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def remove_element(nums, val):
	length = len(nums)
	i = 0
	while length:
		if nums[i] == val:
			nums.pop(i)
			length -= 1
		else:
			i += 1
			length -= 1
	return len(nums)
		

# Example #1:
# Input: nums = [3,2,2,3], val = 3
# Expected Output: 2
# nums should be [2,2,_,_]
# Explanation: Your function should return k = 2,
# with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
nums1 = [3,2,2,3]
val1 = 3
print(remove_element(nums1, val1))

# Example #2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5
# nums should be [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print(remove_element(nums2, val2))