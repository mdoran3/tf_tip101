##########################
# Problem 7: Make Pairs  #
##########################

# Write a function divide_list() that takes in an integer 
# list nums consisting of 2*n integers as parameters. The 
# function divides nums into n pairs such that:

#       Each element belongs to exactly one pair
#       The elements present in a pair are equal

# Return True if nums can be divided into n pairs, 
# otherwise return False.

### U - Understand 
#   What data strcuture would be usful in this scenario?
#   What are we trying to return in this problem?

### P - Plan
#   create an empty set 
#   iterate through nums
#   if num is in the set, delete that num from the set
#   if num is not in set, add it to the set
#   return T/F if the length of the set is 0

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       pairs = set()
#       for num in nums:
#           if num in pairs:
#               delete num from pairs
#           else:
#               add num to pairs
#       return len(pairs) == 0
 
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def divide_list(nums):
    pair = set()
    for num in nums:
        if num in pair:
            pair.remove(num)
        else:
            pair.add(num)
    return len(pair) == 0


nums = [3,2,3,2,2,2]
print(divide_list(nums))
### Example Output: True ###
# Explanation: There are 6 elements in nums, 
# so they should be divided into 6 / 2 = 3 pairs. 
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), 
# it will satisfy all the conditions.

nums = [1,2,3,4]
print(divide_list(nums))
### Example Output: False ###
# Explanation: There is no way to divide nums into 
# 4 / 2 = 2 pairs such that the pairs satisfy every condition.