# Write a function reverse_list() that takes in a list lst and returns 
# elements of the list in reverse order. The list should be reversed 
# in-place without using list slicing (e.g. lst[::-1]).

# Instead, use the two-pointer approach, which is a common technique 
# in which we initialize two variables (also called a pointer in this 
# context) to track different indices or places in a list or string,
# then moves the pointers to point at new indices based on certain 
# conditions. In the most common variation of the two-pointer approach, 
# we initialize one variable to point at the beginning of a list and a 
# second variable/pointer to point at the end of list. We then shift 
# the pointers to move inwards through the list towards each other,
# until our problem is solved or the pointers reach the opposite ends 
# of the list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # INPUT: a list
    # OUTPUT: the same list but reversed
    # Why would we use two pointers to reverse a list?
    # Where do we start the two pointers at?
    # What is the space complexity of this algo?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create two pointer variables - one for the front of the list and one for the end
    # Use a while loop and swap front  and end elements of list until the pointers collide

# 3. Translate each sub-problem into pseudocode:
    # pointer1 = 0
    # pointer2 = len(list) -1
    # while pointer1 less than pointer two:
        # element of list at pointer1 with element of list at pointer2
        # increment pointer1
        # decrement pointer2
    # return the list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

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

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([1, 2, 3, 4, 5, 6]))