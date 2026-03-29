##############################
# PROBLEM 4: FIND THE MIDDLE
##############################

# A variation of the two-pointer technique introduced in Unit 4 
# is to have a slow and a fast pointer that increment at different 
# rates. Given the head of a linked list, use the slow-fast pointer
# technique to find the middle node of a linked list. If there are 
# two middle nodes, return the second middle node.

# Evaluate the time and space complexity of your solution. Define your 
# variables and provide a rationale for why you believe your solution 
# has the stated time and space complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can a slow and fast pointer, on a high level, find a middle?
    # In what case will there be two middle nodes?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set the slow and fast pointer equal to head
    # while fast and fast.next exist
        # increment the slow pointer by 1
        # increment the fast pointer by 2
    # the value at slow should be at center now, retrn it

# 3. Translate each sub-problem into pseudocode:
    # slow = head
    # fast = head
    # while fast and fast.next
        # slow = slow.next
        # fast = fast.next
    # return slow value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

ll = Node(1, Node(2, Node(3)))
print(find_middle_element(ll))

ll2 = Node(1, Node(2, Node(3, Node(4))))
print(find_middle_element(ll2))