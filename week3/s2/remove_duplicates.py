### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What data structure can we use to easily remove items?
    # Is there more than one way to solve this problem?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create an empty list to store the unique values
    # Create a while loop for while the list is still not empty
    # Pop an item of the list and assign it to a variable inside the while loop
    # If the popped variable is not in the unique values list we created, add it to the list
    # Outside the while loop, return the reversed list

# 3. Translate each sub-problem into pseudocode:
    # func(list)
        # uniques {}
        # while loop for list not empty
            # popped = list.pop()
            # if popped not in uniques
                # uniques.append(popped)
        # return reversed uniques

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function remove_duplicates() that takes in a sorted list of 
# integers nums as a parameter and removes all duplicates in the list. 
# The function returns the modified list.

# WITHOUT WHILE LOOP
# def remove_duplicates(nums):
#     uni_nums = set()
#     for num in nums:
#         if num not in uni_nums:
#             uni_nums.add(num)
#     return uni_nums

# WITH WHILE LOOP
def remove_duplicates(nums):
    uni_nums = []
    while nums:
        popped_item = nums.pop()
        if popped_item not in uni_nums:
            uni_nums.append(popped_item)
    return uni_nums[::-1]    

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))