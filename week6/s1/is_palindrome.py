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
    # 

### P - Plan
# 2. Write out in plain English what you want to do: 

# 3. Translate each sub-problem into pseudocode:

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
	pass

# ll = Node(1, Node(2, Node(1)))
# print(is_palindrome(ll))