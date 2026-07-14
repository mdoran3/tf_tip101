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