# Write a function is_prime() that takes in a positive integer n and 
# returns True if it is a prime number and False otherwise. A prime 
# number is a number greater than 1 that has no positive divisors other 
# than 1 and itself.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # INPUT: an integer
    # OUTPUT: A boolean value
    # What makes a number prime?
    # Why are prime numbers important in CS?
    # Should be use a loop?
    # What mathematical operator could be helpful in this problem?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create while loop and decrement down from one below the number until one above number
    # run a modulus
    # if mod == 0 return True
    # if mod never == 0 return False

# 3. Translate each sub-problem into pseudocode:
    # i = n-1
    # while i is greater than 1
        # if n mod i == 0 then it is true
        # else i -+ 1
    # return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_prime(n):
    i = n -1
    while i > 1:
        if n % i == 0:
            return False
        else:
            i -= 1
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))