#####################################
# PROBLEM 4: POSITIVE NEGATIVE PAIRS
#####################################

# Write a function find_largest_k() that takes in a list of 
# integers nums that does not contain any zeroes as a parameter. 
# The function finds the largest positive integer k such that -k 
# also exists in the array and returns k. If there is no such 
# integer, return -1.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Should we initially check for both negatives and positives?
    # Do we need a helper function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # for loop for each number in nums
    # if number is less than 0:
    # if the helper function finds the flipped sign of number in the array, return True
    # else if its pair is not found in helper function, return False
    # back in your main function, if the opposite pair is found, return the number times -1
    # if nothing found ever, return -1

# 3. Translate each sub-problem into pseudocode:

    # def helper_function(num)
        # flipped_num = num * -1
        # if flipped_num in nums
            # return TRUE
        # return FALSE

    # for num in nums
        # if num is not negative    
            # if num thrown into help_function(num) returns TRUE
                # return num * -1
    # return -1
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def find_largest_k(nums):
    def positive_exists(num):
        new_num = num * (-1)
        if new_num in nums:
            return True
        return False

    for num in nums:
        if num < 0:
            if positive_exists(num):
                return num*(-1)
    return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))