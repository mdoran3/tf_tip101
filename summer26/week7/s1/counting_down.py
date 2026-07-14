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