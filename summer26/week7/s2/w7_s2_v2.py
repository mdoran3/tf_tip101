###############################
# Problem 1: Substring Search #
###############################

'''
Given two strings s and sub, write a function count_substring() 
that returns the number of times the substring sub occurs in s. 
Occurrences should not overlap. A substring is a sequence of 
adjacent characters within a larger string.

Your solution must be recursive.

Evaluate the time complexity of your solution.
'''

### U - Understand
#   What should happen once s becomes shorter than sub?
#   Since matches can't overlap, how far should we advance after
#   finding a match versus not finding one?

### P - Plan
'''
1.  Create function definition and pass in s and sub as parameters
2.  if s is shorter than sub, there's no room for a match, so
    return 0
3.  if s starts with sub, count that as one match and recurse on
    the remainder of s after skipping past the whole matched
    substring, adding 1 to the result
4.  otherwise, recurse on s with its first character removed,
    since no match starts here
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN count_substring(s, sub)
    IF length of s is less than length of sub
        RETURN 0
    IF s starts with sub
        RETURN 1 PLUS count_substring(s with the first len(sub)
            characters removed, sub)
    RETURN count_substring(s with its first character removed, sub)
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_substring(s, sub):
	if len(s) < len(sub):
		return 0
	if s.startswith(sub):
		return 1 + count_substring(s[len(sub):], sub)
	return count_substring(s[1:], sub)

print(count_substring("abcdeabcde", "abc"))
'''
Example Usage:

# Example Input: s = "abcdeabcde" sub = "abc"
Example Output:

# Expected Output: 2
# Explanation: 'abc' occurs twice in 'abcdeabcde'

# Time complexity: O(n * m), where n = len(s) and m = len(sub).
# We make up to n recursive calls, and each call does an O(m)
# startswith comparison (plus O(m) slicing when a match is found).
'''


######################################
# Problem 2: How Many 0s (Iterative) #
######################################

'''
Given a sorted list of integers containing only 0s and 1s, 
count the total number of 0’s in the array in O(log n) time.
'''

### U - Understand
#   How does the count of 0s relate to the index of the first 1?
#   How can we find that index in O(log n) time?

### P - Plan
'''
1.  Create function definition and pass in the sorted lst as a
    parameter
2.  set low to 0 and high to the last index of lst
3.  while low is less than or equal to high:
    a.  compute mid, the midpoint between low and high
    b.  if lst[mid] is 1 and (mid is 0 or lst[mid - 1] is 0),
        we found the first 1, so return mid (the count of 0s)
    c.  if lst[mid] is 0, the first 1 must be to the right, so
        move low to mid + 1
    d.  otherwise, the first 1 is at or before mid, so move
        high to mid - 1
4.  if the loop finishes without finding a 1, the list is all 0s,
    so return the length of lst
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN count_zeroes(lst)
    low = 0
    high = length of lst MINUS 1
    WHILE low <= high
        mid = (low + high) DIVIDED BY 2
        IF lst[mid] equals 1 AND (mid equals 0 OR lst[mid - 1] equals 0)
            RETURN mid
        ELSE IF lst[mid] equals 0
            low = mid + 1
        ELSE
            high = mid - 1
    RETURN length of lst
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_zeroes(lst):
	low = 0
	high = len(lst) - 1
	while low <= high:
		mid = (low + high) // 2
		if lst[mid] == 1 and (mid == 0 or lst[mid - 1] == 0):
			return mid
		elif lst[mid] == 0:
			low = mid + 1
		else:
			high = mid - 1
	return len(lst)

print(count_zeroes([0, 0, 0, 0, 1, 1, 1]))
'''
Example Usage:

# Example Input: [0, 0, 0, 0, 1, 1, 1]
Example Output:

# Expected Output: 4
'''


######################################
# Problem 3: How Many 0s (Recursive) #
######################################

'''
Implement count_zeroes() recursively.
'''

### U - Understand
#   How does the count of 0s relate to the index of the first 1?
#   How do we carry the search bounds (low/high) across recursive calls?

### P - Plan
'''
1.  Create function definition and pass in the sorted lst, plus
    low and high indices as parameters, defaulting low to 0 and
    high to None so callers don't have to pass them
2.  on the first call, if high is None, set it to the last index
    of lst
3.  base case: if low is greater than high, there was no 1 found
    in range, so return the length of lst
4.  compute mid, the midpoint between low and high
5.  if lst[mid] is 1 and (mid is 0 or lst[mid - 1] is 0), we
    found the first 1, so return mid (the count of 0s)
6.  if lst[mid] is 0, the first 1 must be to the right, so
    recurse with low set to mid + 1
7.  otherwise, the first 1 is at or before mid, so recurse with
    high set to mid - 1
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN count_zeroes(lst, low, high)
    IF high is not set
        high = length of lst MINUS 1
    IF low > high
        RETURN length of lst
    mid = (low + high) DIVIDED BY 2
    IF lst[mid] equals 1 AND (mid equals 0 OR lst[mid - 1] equals 0)
        RETURN mid
    ELSE IF lst[mid] equals 0
        RETURN count_zeroes(lst, mid + 1, high)
    ELSE
        RETURN count_zeroes(lst, low, mid - 1)
END		
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_zeroes(lst, low=0, high=None):
	if high is None:
		high = len(lst) - 1
	if low > high:
		return len(lst)
	mid = (low + high) // 2
	if lst[mid] == 1 and (mid == 0 or lst[mid - 1] == 0):
		return mid
	elif lst[mid] == 0:
		return count_zeroes(lst, mid + 1, high)
	else:
		return count_zeroes(lst, low, mid - 1)

print(count_zeroes([0, 0, 0, 1, 1, 1, 1]))
'''
Example Usage:

# Example Input: [0, 0, 0, 1, 1, 1, 1]
Example Output:

# Expected Output: 3
'''