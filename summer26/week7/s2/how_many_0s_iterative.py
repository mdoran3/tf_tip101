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