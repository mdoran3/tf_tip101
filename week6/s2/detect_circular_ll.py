##########################################
# PROBLEM 1: DETECT CIRCULAR LINKED LIST
##########################################

# A circular linked list is a linked list where the tail node points
# at the head node. Given the head of a linked list, write a function 
# is_circular() that returns True if the linked list is circular and 
# False otherwise.

# Note: a circular list is more than just a cycle - specifically 
# connecting the first and last nodes.

# Evaluate the time and space complexity of your solution. Define 
# your variables and provide a rationale for why you believe your 
# solution has the stated time and space complexity.


### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What makes a linked list circular?
    # What should we be comparing in the LL during our iterations?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set currnet equal to head.next in order to compare curent and head
    # Use a while loop while current and current not equal to head
    # Iterate current to the next node
    # outside while loop return current == to head (T or F)

# 3. Translate each sub-problem into pseudocode:
    # current = head.next
    # while current exists and current does not equal head
        # current = current.next
    # return current equals head (True of False return)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    current = head.next
    while current and current != head:
        current = current.next
    return current == head

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
print(is_circular(num1))

# var1 -> var2 -> var3
var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
print(is_circular(var1))