###############################
# Problem 6: Has Many Smaller #
###############################

# Write a function smaller_numbers_than_current() 
# that takes in a list of numbers nums as a parameter. 
# For each nums[i], the function should find out how 
# many numbers in the list are smaller than it. 
# (For each nums[i], count the number of valid j's 
#  such that j!=i and nums[j] < nums[i])

# Return the answers in a list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What does the sum() function do in Python?
#   What are we returning?

### P - Plan
#   create and empty list
#   run the sum() function with ++1 and iterate through nums
#   if num < num it will add one and then append to the empty list
#   return the list

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       lst = []
#       for num in nums
#           count = sum(1 for n in nums if n < num)
#           lst.append(count)
#       return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def smaller_numbers_than_current(nums):
    length = len(nums)
    i = 0
    ticks = 0
    count = []
    while i < length:
        curr = nums[i]
        for num in nums:
            if num < curr:
                ticks += 1
        count.append(ticks)
        ticks = 0
        i += 1
    return count

# Co-authored by Claude AI
def smaller_numbers_than_current_v2(nums):
    result = []
    for num in nums:
        count = sum(1 for n in nums if n < num)
        result.append(count)
    return result

# Co-authored by Claude AI
def smaller_numbers_than_current_v3(nums):
    return [sum(1 for n in nums if n < num) for num in nums]

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))
# Example Output: [4,0,1,1,3]

print(smaller_numbers_than_current_v2(nums))
# Example Output: [4,0,1,1,3]

print(smaller_numbers_than_current_v3(nums))
# Example Output: [4,0,1,1,3]