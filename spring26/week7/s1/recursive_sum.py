############################
# PROBLEM 3: RECURSIVE SUM
############################

# Without using the built-in sum() function, write a function 
# sum_list() that calculates the sum of all values in a list 
# recursively.

# What is the time complexity of this function? What is the 
# space complexity?
    # time complexity = O(N)
    # space complexity = O(1)

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # When solving recursive problems, we should start by asking, 
        # what is the base case?
    # How can we use recursion by continually passing in a modified list?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # If the list does not exist, return 0
    # set a variable for number that is popped from the lst 
    # return that popped variable + recursive call to sum_list(lst)
        # your new list will have one less element that was popped off the end. 

# 3. Translate each sub-problem into pseudocode:
    # func(lst)
        # if lst doesn't exist:
            # return 0
        # element = lst.pop()
        # return element + func(lst)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def sum_list(lst):
	if not lst:
		return 0
	popped = lst.pop()
	return popped + sum_list(lst)	

print(sum_list([1,2,3,4,5]))