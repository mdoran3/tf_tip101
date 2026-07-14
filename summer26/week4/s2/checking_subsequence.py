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