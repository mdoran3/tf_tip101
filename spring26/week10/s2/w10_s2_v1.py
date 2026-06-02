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


#################################################
# PROBLEM 3: GREATEST COMMON DIVISOR OF STRINGS #
#################################################

# For two strings s and t, we say "t divides s" if and 
# only if s = t + t + t + ... + t + t (i.e., t is concatenated 
# with itself one or more times).

# Given two strings str1 and str2, return the largest string 
# x such that x divides both str1 and str2.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # If no common divisor exists, should we return an empty string or None?
    # Can the two strings be the same, and if so, is the answer just the string itself?

### P - Plan
# 2. Write out in plain English what you want to do:
    # first check if a common divisor can even exist by seeing if str1 + str2 equals str2 + str1
    # if they're not equal, return an empty string
    # otherwise, find the gcd of the two string lengths using the euclidean algorithm
    # return the first gcd-length characters of str1 as the answer

# 3. Translate each sub-problem into pseudocode:
    # if str1 + str2 is not equal to str2 + str1, return ""
    # set a to the length of str1, set b to the length of str2
    # while b is not 0, set a to b and b to a mod b
    # return str1 sliced from 0 to a

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# from math import gcd
# def gcd_of_stings(str1, str2):
# 	if str1 + str2 != str2 + str1:
# 		return ""
# 	return str1[:gcd(len(str1), len(str2))]

def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    a, b = len(str1), len(str2)
    while b:
        a, b = b, a % b
    return str1[:a]

# Example #1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
str1 = "ABCABC"
str2 = "ABC"
print(gcd_of_strings(str1, str2))

# Example #2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
str1 = "ABABAB"
str2 = "ABAB"
print(gcd_of_strings(str1, str2))

# Example #3:
# Input: st1 = "LEET", str2 = "CODE"
# Output: ""
st1 = "LEET"
str2 = "CODE"
print(gcd_of_strings(str1, str2))


#########################################
# PROBLEM 4: CHECK BALANCED BINARY TREE #
#########################################

# Given the root of a binary tree, return True 
# if the tree is balanced and False otherwise.

# A balanced binary tree is a binary tree in 
# which the depth of the two subtrees of every 
# node never differs by more than one.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#    a. What should we return for an empty tree (None root)?
#    b. Does "balanced" apply to every node in the tree, or just the root?

### P - Plan
# 2. Write out in plain English what you want to do:
#    Recursively compute the height of each subtree. At every node, check if the
#    left and right subtree heights differ by more than 1. If any node is
#    unbalanced, propagate a sentinel value (-1) back up to short-circuit the
#    rest of the traversal. Return True if the final height is not -1.

# 3. Translate each sub-problem into pseudocode:
#    define dfs(node):
#        if node is None: return 0
#        left_height = dfs(node.left)
#        if left_height == -1: return -1          # already unbalanced
#        right_height = dfs(node.right)
#        if right_height == -1: return -1         # already unbalanced
#        if abs(left_height - right_height) > 1: return -1   # this node unbalanced
#        return 1 + max(left_height, right_height)
#
#    return dfs(root) != -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def is_balanced(root):
    if not root:
        return True

    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        if left_height == -1:
            return -1
        right_height = dfs(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return dfs(root) != -1




# Input Tree #1:

#       3
#      /  \
#     9   20
#        /  \
#       15   7
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(is_balanced(root1))  # Expected: True


# Input Tree #2:

#           1
#          / \
#         2   2
#        / \
#       3   3
#      / \
#     4   4

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)
print(is_balanced(root2))  # Expected: False


# Input Tree #3: Empty Tree
root3 = None
print(is_balanced(root3))  # Expected: True


####################################
# PROBLEM 5: SUBARRAY SUM EQUALS K #
####################################

# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum 
# equals to k.

# A subarray is a contiguous non-empty sequence of 
# elements within an array.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#    - Can nums contain negative integers? (Yes — this rules out a sliding window approach)
#    - Can the same element be part of multiple counted subarrays? (Yes — subarrays can overlap)

### P - Plan
# 2. Write out in plain English what you want to do:
#    Track a running prefix sum as we iterate through the array. At each index, check
#    how many times we've previously seen (prefix_sum - k) — each occurrence means there's
#    a subarray ending here that sums to k. Store each prefix sum in a hash map as we go.

# 3. Translate each sub-problem into pseudocode:
#    - Initialize count = 0, prefix_sum = 0, seen = {0: 1}
#    - For each num in nums:
#        - Add num to prefix_sum
#        - Add seen[prefix_sum - k] to count (0 if not present)
#        - Increment seen[prefix_sum] by 1
#    - Return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def subarray_sum(nums, k):
	count = 0
	prefix_sum = 0
	seen = {0: 1}

	for num in nums:
		prefix_sum += num
		count += seen.get(prefix_sum - k, 0)
		seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

	return count
			

# Example #1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2
nums = [1, 1, 1]
k = 2
print(subarray_sum(nums, k))

# Example #2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2
nums = [1, 2, 3]
k = 3
print(subarray_sum(nums, k))