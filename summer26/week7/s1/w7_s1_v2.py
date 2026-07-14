############################
# Problem 1: Counting Down #
############################
'''
A recursive function is a function that calls itself within the body 
of the function.

Step 1: Copy this code into your IDE and run it.

Step 2: Then create another function countdown_iterative() that produces 
the same output without using recursion.

Compare your iterative (non-recursive) solution to the recursive solution 
provided. What is similar? What is different?
'''

### U - Understand
#   In your own words, describe recursion.
#   What does an iterative version of a recursion funtion
#       typically include?

### P - Plan
'''
1.  Create function definition with one parameter 'n'
2.  Create a while loop for while n is greater than 0
3.  Print 'n' at every iteration
4.  Decrement 'n' by 1
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN countdown_iterative(n)
    WHILE n is greater than 0 DO
        PRINT n to console
		DECREMENT n by 1
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def countdown(n):
	if n > 0:
		print(n)
		countdown(n - 1)
		
print("\nCOUNTDOWN RECURSIVE")	
countdown(5)

def countdown_iterative(n):
	while n > 0:
		print(n)
		n -= 1
		
print("\nCOUNTDOWN ITERATIVE")
countdown_iterative(5)

'''
Example Usage:

# Example Input: 5
Example Output:

# Expected Output:
# 5
# 4
# 3
# 2
# 1
# Explanation: The function prints numbers starting at 5 
# and counts down by 1 until it reaches 1.
'''


##############################
# Problem 2: Fibonacci Cases #
##############################
'''
Given the base case and recursive case, write a function fibonacci() 
that returns the nth number in the fibonacci sequence. The Fibonacci 
sequence is a mathematical sequence of numbers where each number is 
the sum of the two preceding numbers.

Base Cases: Because Fibonacci numbers are defined by adding the two 
previous numbers in the sequence, the first two Fibonacci numbers are 
pre-defined. By definition, the 0th Fibonacci number is 0, and the 1st 
Fibonacci number is 1.

Recursive Case: The nth Fibonacci number is the n-1th Fibonacci number 
+ the n-2th Fibonacci number.
'''

### U - Understand
#   What is a base case in recursion?
#   Can we make multiple recursive calls at a time?

### P - Plan
'''
1.  Create function definition and pass in an integer as a parameter
2.  if n equals 0 then return 0
3.  if n equals 1 then return 1
4.  return the sum of two recursive calls with parameters n-1 and
    n-2 respectively.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN fibonacci(n)
    IF n is equal to 0
        RETURN 0
	IF n is equal to 1
        RETURN 1
	RETURN fibonacci of n-1 PLUS fibonacci of n-2
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
'''
# Example Input: 6
Example Output: 8

# Expected Output: 8
# Explanation: The 6th Fibonacci number is 8. The 5th Fibonacci 
# number is 5 and the 4th Fibonacci
# number is 3. 5 + 3 = 8.
'''


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