def max_difference(lst):
    max_num = float('-inf')
    min_num = float('inf')
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num - min_num

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # When keeping track of max and min numbers, what number should we initialize them to?
    # What do we compare at each loop iteration?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes a list as input
    # Initialize max_num to negative infinity and min_num to positive infinity
    # Iterate through each number in the list and compare it to max_num and min_num
    # If the number is greater than max_num, update max_num to be that number
    # If the number is less than min_num, update min_num to be that number
    # After iterating through the list, return the difference between max_num and min_num
# 3. Translate each sub-problem into pseudocode:
    # func(list):
    #     max_num = -inf
    #     min_num = inf
    #     for each num in list:
    #         if num > max_num:
    #             max_num = num
    #         if num < min_num:
    #             min_num = num
    #     return max_num - min_num

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def max_difference(lst):
    max_num = float('-inf')
    min_num = float('inf')
    for num in lst:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num - min_num
