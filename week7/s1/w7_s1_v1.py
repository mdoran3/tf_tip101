#########################
# PROBLEM 1: HELLO HELLO
#########################

# A recursive function is a function that calls itself within 
# the body of the function.

# Step 1: Copy the recursive function repeat_hello() into your
# IDE and run it.

# Step 2: Then create another function repeat_hello_iterative() 
# that produces the same output without using recursion.

# Compare your iterative (non-recursive) solution to the recursive 
# olution provided. What is similar? What is different?

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is recursion?
    # What is a base case?
    # What is a call stack?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a while loop while the param is greater than 0
    # In the while loop use a print function to print the desired message
    # decrement n by 1

# 3. Translate each sub-problem into pseudocode:
    # func repeat_hello_iterative(n):
        # while n greater than n:
            # print(message)
            # n = n -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
def repeat_hello_iterative(n):
	while n > 0:
		print("Hello")
		n -= 1
		
repeat_hello(5)
repeat_hello_iterative(5)

#############################
# PROBLEM 2: FACTORIAL CASES
#############################

# Given the base case and recursive case, write a function 
# factorial() that returns the factorial of a non-negative 
# integer n. The factorial of a number is the product of all 
# numbers between 1 and n.

# Base Case: The smallest number we can find a factorial of 
# is 0. By definition, the factorial of 0 is 1.

# Recursive Case: We can restate the problem to say that the 
# factorial of n is n * the factorial of n-1.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Since 0 is the lowest number factorial is useful for, what is
        # the base case and what does it return?
    # How can we eventually hit our base case with factorial?
    # How can we use the call stack in this problem?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # write base case if n equal 0 and return 1
    # return n + call factorial with n = n-1

# 3. Translate each sub-problem into pseudocode:
    # func(n):
        # if n is equal to 0:
            # return 1
        # return n * func(n-1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def factorial(n):
	if n == 0:
		return 1
	return n * factorial(n-1)

print(factorial(5))

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

###################################
# PROBLEM 4: RECURSIVE POWER OF 2
###################################

# Given an integer n, return True if n is a power 
# of two. Otherwise, return `False``.

# An integer n is a power of two if there exists an 
# integer x such that n == 2ˣ.

# Solve the problem recursively. What is the time 
# complexity of this function? What is the space 
# complexity?

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is the base case?
    # What do we put as a parameter into our recursive call?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if the parameter equals 2, we can return True
    # if n modulus 2 does not equal 0 or if n is less than 2, we returh False
    # make a recursive called with n / 2

# 3. Translate each sub-problem into pseudocode:
    # func(n):
        # if n equals 2: 
            # return True
        # if n mod 2 is not equal to 0 or n < 2:
            # return False
        # return func(n/2)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_power_of_two(n):
	if n == 2:
		return True
	if n % 2 != 0 or n < 2:
		return False
	return is_power_of_two(n/2)

print(is_power_of_two(16))
print(is_power_of_two(18))

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