##############################
# Problem 6: Below Threshold #
##############################

# Write a function count_less_than() that takes in a 
# list of integers numbers and an integer threshold as 
# parameters and returns the number of items in numbers 
# that are less than threshold.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How many times do we need to iterate through this list?
#   What would the asymptotic time complexity be of this algorithm?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   create a variable that tracks the count or frequency
#   iterate through the list
#   check each number and see if it less than threshold
#   if it is less than threshold, add it to count

# 3. Translate each sub-problem into pseudocode:
#   func(numbers, threshold)
#       for num in numbers
#           if num < threshold
#               count ++  
#       return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count += 1
    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)


#########################
# Problem 7: Evens List #
#########################

# Write a function get_evens() that takes in a list 
# of integers lst as a parameter and returns a list 
# of all even numbers in the list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is the space complexity of this algorithm and why?
#   What key mathematical feature, often used in CS, whill be utilized 
#       in this problem for find evens?

### P - Plan
# 2. Write out in plain English what you want to do: 
#   Create an evens list variable
#   Iterate through the lst
#   Check if each number in list is even
#   If it is even, add it to the evens list
#   return evens list

# 3. Translate each sub-problem into pseudocode:
#   func(lst):
#       evens = []
#       for num in lst:
#           if num is even
#               append to evens
#       return evens

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def get_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)


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