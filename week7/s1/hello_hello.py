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