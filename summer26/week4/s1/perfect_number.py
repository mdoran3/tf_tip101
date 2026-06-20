##############################
# Problem 1: Perfect Number  #
##############################

'''
Write a function is_perfect_number() that takes in a 
positive integer n and returns True if it is a perfect 
number and False otherwise. A perfect number is a 
positive integer that is equal to the sum of its proper 
divisors, excluding itself.

For example, 6 is a perfect number because its divisors 
or 1, 2, and 3 and 1 + 2 + 3 = 6.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What mathematical operator would be helpful in this problem?
#   What type of loop could we use and why?

### P - Plan
#   Create an empty list to store the divisors
#   Go through all numbers 1 to n-1 and find ones that are divisors
#   Add the divisors to the empty list
#   Sum the list and check if it equals n

# 3. Translate each sub-problem into pseudocode:
'''
    func(n):
        divisors = empty list
        i = n -1
        while n > 0
            if i mod n == 0, append i to divisors
            decrement i by 1
        summation_of_divisors = sum of nums in divisiors list
        if summarion_of_divisors == n
            return True
        else:
            return False
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_perfect_number(n):
    divisors = []
    i = n-1
    while i > 0:
        if n % i == 0:
            divisors.append(i)
        i -= 1
    total = sum(divisors)
    return total == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))


'''

Example Output:

True
True
False

'''