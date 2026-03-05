### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What are data types and why might they be important in this problem?
    # What is the difference of 10 and "10" to a computer?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a variable called sum and set it equal to 0
    # Iterate through the list of strings
    # Cast each string item to and integer
    # Add that integer to the rolling sum variable

# 3. Translate each sub-problem into pseudocode:
    # func(str):
        # sum = 0
        # for loop : list/str
            # cast str to int
            # add int to sum
        # return sum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
    
# Write a function sum_of_number_strings() that takes in a list of strings 
# nums. Each string is a representations of integers. The function should 
# return the sum of these strings as an integer.

def sum_of_number_strings(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)