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