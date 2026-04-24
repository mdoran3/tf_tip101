##############################
# PROBLEM 5: BINARY SEARCH I
##############################

# Binary search is a searching algorithm that allows 
# us to efficiently find the index of a given value 
# within a sorted list. Given the pseudo code for 
# binary search below, implement an iterative (non-recursive) 
# implementation of binary search. There is also a 
# recursive alternative that we’ll cover in the session 
# 2 problem set!

# Evaluate the time and space complexity of your 
# implementation.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is the asymptotic time complexity of this algorithm?
    # How do we use the pointers in this algorithm?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Initialize each pointer
    # set a while loop for while left is less than right
        # set middle equal to (right+left) // 2
        # if middle value is target
            # return middle
        # else if middle value is less than target
            # move the left pointer to middle + 1
        # else
            # move the right pointer to middle - 1
    # return -1 if nothing is found

# 3. Translate each sub-problem into pseudocode:
    # follow the pseudo code below

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	left = 0
	# Initialize a right pointer to the last index in the list
	right = len(lst) - 1
	
	# While left pointer is less than right pointer:
	while left < right:
		# Find the middle index of the array
		middle = (left+right) // 2      # IMPORTANT - Integer division using // not /
		# If the value at the middle index is the target value:
		if lst[middle] == target:
			# Return the middle index
			return middle
		# Else if the value at the middle index is less than our target value:
		elif lst[middle] < target:
			# Update pointer(s) to only search right half of the list in next loop iteration
			left = middle + 1
		# Else
		else:
			# Update pointer(s) to only search left half of the list in next loop iteration
			right = middle - 1
	# If we search whole list and haven't found target value, return -1
	return -1

def binary_search_recursive(lst, target):
	if not lst:
		return -1
	middle = len(lst) // 2
	if lst[middle] == target:
		return middle
	elif lst[middle] < target:
		result = binary_search_recursive(lst[middle+1:], target)
		return -1 if result == -1 else result + middle + 1
	else:
		return binary_search_recursive(lst[:middle], target)

lst = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(lst, 11))
print(binary_search_recursive(lst, 11))