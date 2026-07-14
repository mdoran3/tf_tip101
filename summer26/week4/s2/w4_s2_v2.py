################################
# Problem 1: Merge Sorted List #
################################

'''
The two-pointer approach is a common technique in which we initialize two 
variables (also called a pointer in this context) to track different 
indices or places in a list or string, then moves the pointers to point 
at new indices based on certain conditions. A common variation of this 
technique is to point one variable at the beginning of one list/string 
and a second pointer at the beginning of a second list/string, then 
increment each pointer conditionally to solve a problem.

Using the two pointer approach, write a function merge_sorted_lists() 
that takes in two sorted lists lst1 and lst2 as parameters and merges 
them into a single sorted list. The function returns the new list.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   Is each individual list sorted?
#   What type of conditional check must we make with the pointers?

### P - Plan
'''
    Set both pointers to 0
    Create a new empty list
    Use a while loop for while the pointers are less than the length of the lists
    Compare elements of both lists and append the smaller one to the new list
    At the end, extend the new list with each of the parameter list in case of extra elements
    Return the new list
'''

# 3. Translate each sub-problem into pseudocode:
'''
FUNCTION merge_sorted_lists(lst1, lst2):
    SET p1 = 0
    SET p2 = 0
    SET new_list = []

    WHILE p1 < length of lst1 AND p2 < length of lst2:
        IF lst1[p1] < lst2[p2]:
            APPEND lst1[p1] to new_list
            INCREMENT p1
        ELSE:
            APPEND lst2[p2] to new_list
            INCREMENT p2

    EXTEND new_list with remaining elements of lst1 starting at p1
    EXTEND new_list with remaining elements of lst2 starting at p2

    RETURN new_list
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def merge_sorted_lists(lst1, lst2):
    p1 = 0
    p2 = 0
    new_list = []
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] < lst2[p2]:
            new_list.append(lst1[p1])
            p1 += 1
        else:
            new_list.append(lst1[p2])
            p2 += 1
    new_list.extend(lst1[p1:])
    new_list.extend(lst2[p2:])
    return new_list
    

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)

'''
Example Output:

[1, 2, 3, 4, 5, 6]
'''


###################################
# Problem 2: Checking Subsequence #
###################################

'''
Write a function is_subsequence that takes in two strings s and t 
as parameters and returns True if s is a subsequence of t and 
False otherwise.

A subsequence of a string is a new string that is formed from the 
original string by deleting some or none of the characters without 
disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How can you pull an index from a list?
#   What could the return statement look like? Would an assertion
#       statement work that returns a boolean?

### P - Plan
'''
    Create an empty list to store the indices of matched characters
    Loop through each character in s
        - If the character exists in t, record its index and add to list
        - If the character does not exist in t, return False immediately
    After the loop, check if the indices list is already sorted
        - If sorted, the characters appear in order → return True
        - Otherwise return False
'''

# 3. Translate each sub-problem into pseudocode:
'''
indices = []
for each char in s:
    if char in t:
        idx = index of char in t
        append idx to indices
    else:
        return False
return indices == sorted(indices)
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_subsequence(s, t):
	indices = []
	for char in s:
		if char in t:
			idx = t.index(char)
			indices.append(idx)
		if char not in t:
			return False
	# print(indices)            # DEBUG
	# print(sorted(indices))    # DEBUG
	return indices == sorted(indices)
    

s = "abc"
t = "ahbgdc"
print(is_subsequence(s, t))

a = "cba"
b = "ahbgdc"
print(is_subsequence(a, b))

'''
Example Output:

True
False
'''


##################################
# Problem 3: Sort List by Parity #
##################################

'''
Write a function sort_array_by_parity() that takes in a list of 
integers nums where half of the integers are odd, and the other 
half are even. The function sorts the list so that whenever nums[i] 
is odd, i is odd and whenever nums[i] is even, i is even. The function 
returns the list in any order that satisfies the condition.
'''

### U - Understand
#   Since half the integers are even and half are odd, does that guarantee every
#       even index has a matching odd index to swap with if needed?
#   Does the relative order of even numbers among even indices (or odd among odd)
#       matter, or just that each lands in a same-parity index?

### P - Plan
'''
Use two pointers — one starting at index 0 (even lane) and one at index 1 (odd lane),
each advancing by 2 to stay in their lane.

    Walk the even pointer forward (by 2) until we find an odd number sitting at an even index.
    Walk the odd pointer forward (by 2) until we find an even number sitting at an odd index.
    Swap those two misplaced elements.
    Repeat until both pointers go out of bounds.
    Return the modified list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
even = 0
odd = 1

while even < len(nums) and odd < len(nums):
    while even < len(nums) and nums[even] is even:
        even += 2
    while odd < len(nums) and nums[odd] is odd:
        odd += 2
    if both pointers still in bounds:
        swap nums[even] and nums[odd]

return nums
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sort_array_by_parity(nums):
    even, odd = 0, 1
    while even < len(nums) and odd < len(nums):
        while even < len(nums) and nums[even] % 2 == 0:
            even += 2
        while odd < len(nums) and nums[odd] % 2 == 1:
            odd += 2
        if even < len(nums) and odd < len(nums):
            nums[even], nums[odd] = nums[odd], nums[even]
    return nums


nums = [4,2,5,7]
nums2 = [2,3]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

'''
Example Output:

[4,5,2,7]
# [2,7,4,5], [2,7,4,5], [4,7,2,5] also works
[2,3]
'''