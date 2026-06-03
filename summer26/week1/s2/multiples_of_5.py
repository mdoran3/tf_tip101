#############################
# Problem 8: Multiples of 5 #
#############################

# Write a function multiples_of_five() that prints 
# out multiples of 5 between 1 and 100 (inclusive).

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What key mathematical operator is used in this function?
#   Do we have to iterate through all numbers 1 -100?
#   What does this function return?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   Iterate through numbers ranging from 1 - 100 
#   Check if each number is a multiple of 5
#   If it is, print it to the console

# 3. Translate each sub-problem into pseudocode:
#   func(lst):
#       for num in range(1, 101)
#           if num is multiple of 5
#               print num

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def multiples_of_five():
    for num in range(1, 101):
        if num % 5 == 0:
            print(num)   

multiples_of_five()