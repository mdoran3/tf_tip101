################################
# Problem 1: Merge Sorted List #
################################

'''
The two-pointer approach is a common technique in which we initialize two 
variables (also called a pointer in this context) to track different 
indices or places in a list or string, then moves the pointers to point 
at new indices based on certain conditions. A common variation of this 
technique is to point one variable at the beginning of one list/string 
and a second pointer at the beginning of a second list/string, then 
increment each pointer conditionally to solve a problem.

Using the two pointer approach, write a function merge_sorted_lists() 
that takes in two sorted lists lst1 and lst2 as parameters and merges 
them into a single sorted list. The function returns the new list.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   Is each individual list sorted?
#   What type of conditional check must we make with the pointers?

### P - Plan
'''
    Set both pointers to 0
    Create a new empty list
    Use a while loop for while the pointers are less than the length of the lists
    Compare elements of both lists and append the smaller one to the new list
    At the end, extend the new list with each of the parameter list in case of extra elements
    Return the new list
'''

# 3. Translate each sub-problem into pseudocode:
'''
FUNCTION merge_sorted_lists(lst1, lst2):
    SET p1 = 0
    SET p2 = 0
    SET new_list = []

    WHILE p1 < length of lst1 AND p2 < length of lst2:
        IF lst1[p1] < lst2[p2]:
            APPEND lst1[p1] to new_list
            INCREMENT p1
        ELSE:
            APPEND lst2[p2] to new_list
            INCREMENT p2

    EXTEND new_list with remaining elements of lst1 starting at p1
    EXTEND new_list with remaining elements of lst2 starting at p2

    RETURN new_list
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def merge_sorted_lists(lst1, lst2):
    p1 = 0
    p2 = 0
    new_list = []
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] < lst2[p2]:
            new_list.append(lst1[p1])
            p1 += 1
        else:
            new_list.append(lst1[p2])
            p2 += 1
    new_list.extend(lst1[p1:])
    new_list.extend(lst2[p2:])
    return new_list
    

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged_lst = merge_sorted_lists(lst1, lst2)
print(merged_lst)

'''
Example Output:

[1, 2, 3, 4, 5, 6]
'''