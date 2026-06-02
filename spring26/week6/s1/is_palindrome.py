############################
# PROBLEM 5: IS PALINDROME
############################

# Given the head of a singly linked list, return True if the 
# values of the linked list are palindromic and False otherwise. 
# Use the two-pointer technique in your solution.

# Evaluate the time and space complexity of your solution. 
# Define your variables and provide a rationale for why you 
# believe your solution has the stated time and space complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Arrays can be simple to find palindromes, but what makes it 
        # a bit harder with linked lists?
    # What must be compared to check if a palindrome is present?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if there are no nodes or only one node in the LL: return True
    # set two pointers, slow and fast, equal to head
    # use a while loop to check for fast and fast.next
    # Move slow forward one and fast forward two on every iteration until 
        # the while loop closes. 
    # Now slow is in position
    # Set a prev variable to none and reverse the second half of the list
    # do a while looop while slow
        # create a temp node and set it equal to slow.next
        # set  slow.next equal to prev
        # set prev equal to slow
        # now set slow equal to temp
    # Create a left and right pointer
    # do a while loop while right 
        # if left val does not equal right val          
             # return False
        # move left up one
        # move right up one
    # return True

# 3. Translate each sub-problem into pseudocode:
    # if head == None or head.next == None:
        # return True

    # slow, fast = head
    # while fast and fast.next:
        # slow = slow.next
        # fast = fast.next.next

    # prev = None
    # while slow:
        # temp = slow.next
        # slow.next = prev
        # prev = slow
        # slow = temp

    # left = head
    # right = prev
    # while right:
        # if left.val not equal to right.val:
            # return False
        # left = left.next
        # rigth = right.next
    # return True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

# def is_palindrome(head):
#     current = head
#     vals = []
#     while current:
#         vals.append(current.value)
#         current = current.next
#     vals_rev = vals[::-1]
#     if vals == vals_rev:
#         return True
#     return False
    
# ll = Node(1, Node(2, Node(1)))
# print(is_palindrome(ll))

# ll2 = Node(1, Node(2, Node(1, Node(1))))
# print(is_palindrome(ll2))

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def is_palindrome(head):
    if head is None or head.next is None:
        return True
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp_node = slow.next
        slow.next = prev
        prev = slow
        slow = temp_node

    left = head
    right = prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    return True   

ll = Node(1, Node(2, Node(1)))
print(is_palindrome(ll))