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