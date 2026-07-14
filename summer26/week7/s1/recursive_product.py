################################
# Problem 3: Recursive Product #
################################

'''
Write a function list_product() that calculates the product 
of all values in a list recursively.

What is the time complexity of this function? What is the 
space complexity?
'''

### U - Understand
#   How can slicing help us here?
#   Do we need a helper frunction?

### P - Plan
'''
1.  Create function definition and pass in a list as a parameter
2.  if the list is empty then return 1
3.  return the first element of the list multiplied by a recursive
    call with the rest of the list (everything after the first
    element) as the parameter
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN list_product(lst)
    IF lst is empty
        RETURN 1
	RETURN lst[0] TIMES list_product of the rest of lst
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def list_product(lst):
	if len(lst) == 0:
		return 1
	return lst[0] * list_product(lst[1:])

print(list_product([1,2,3,4,5]))
'''
Example Usage:

# Example Input: [1, 2, 3, 4, 5]
Example Output:

# Expected Output: 120
# Explanation: 1 * 2 * 3 * 4 * 5 = 120
'''