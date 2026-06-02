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