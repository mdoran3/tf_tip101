##################################
# PROBLEM 1: CONTAINS DUPLICATES #
##################################

# Given an integer array nums, return True if any value appears 
# at least twice in the array, and return False if every element
# is distinct.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we use a dictionary to our advantage?
    # Can we automatically return True at a certain step? Which step?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create an empty dictionary
    # iterate through the nums array
    # if a number in the nums array is not in dictionary we created, add it
    # else if it is in there, we can just return True because we found a duplicate
    # if we go through the whole list and do not find a duplicate, we just return False

# 3. Translate each sub-problem into pseudocode:
    # def func(nums)
        # dict = {}
        # for number in nums
            # if number not in dict:
                # dict[number] = 1
            # else:
                # return True
        # return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def contains_duplicate(nums):
	nums_dict = {}
	for num in nums:
		if num not in nums_dict:
			nums_dict[num] = 1
		else:
			return True
	return False

# Example #1: 
# Input: nums = [1,2,3,1]
# Output: True
nums = [1,2,3,1]
print(contains_duplicate(nums))

# Example #2:
# Input: nums = [1,2,3,4]
# Output: False
nums1 = [1,2,3,4]
print(contains_duplicate(nums1))

# Example #3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True
nums2 = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums2))