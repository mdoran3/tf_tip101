#########################
# PROBLEM 3: REMOVE TAIL
#########################

# The following code attempts to remove the tail 
# of a singly linked list. However, it has a bug!

# Step 1: Copy this code into your IDE.

# Step 2: Create your own test cases to run the
# code against, and use print statements and the 
# stack trace to identify and fix the bug so that 
# the function correctly removes the tail of the 
# list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is an off by one error?
    # What are a few ways to debug code to get to a solution?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # run a debugger and step through problem
    # check for off by one errors and adjust 
    # add print statements

# 3. Translate each sub-problem into pseudocode:
    # while current.next.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next        

     
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

ll = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_tail(ll))