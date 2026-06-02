# The reverse_list() problem can also be solved without using the two 
# pointer technique (as you may have seen it in previous units)! Evaluate 
# the time and space complexity of your two-pointer solution.

# Then, evaluate the time and space of the following solution:

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is asymptotic time complexities and how are they noted?
    # What is space complexity?
    # What are considered some of the best times and worst times?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # ALGO 1:
        # Time Complexity: O(n) + O(n) = O(n)
            # List is iterated through once while slicing
            # List is iterated through againt to put back into original list
            # Time complexities are not concerned with factors so => O(n)
        # Space Complexity: O(n)
            # A new list, reverse_list, is created with n elements, so => O(n)

    # ALGO 2
        # Time Complexity: O(n/2) = O(n)
            # With two pointers, list is iterated through n/2 times
            # Time complexity is not concerned with factors so O(n/2) => O(n)
        # Space Complexity: O(1)
            # The list is reversed by operating on the original list and no copy is made

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# ALGO 1
def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]

# ALGO 2
def reverse_list(lst):
    front = 0
    back = len(lst) - 1

    while front < back:
        temp = lst[front]
        lst[front] = lst[back]
        lst[back] = temp
        front += 1
        back -= 1
    return lst