#################################
# Problem 3: Remove First Value #
#################################

'''
The following code attempts to remove the first node 
with a given value from a singly linked list based 
but it contains a bug!

Step 1: Copy this code into your IDE.

Step 2: Create your own test cases to run the code 
against, and use print statements and the stack 
trace to identify and fix the bug so that the function 
correctly removes a node by value from the list.
'''

### U - Understand
#   Whats the first thing we should do when inspecting a bug in the code?
#   What do a lot of errors end up being caused from?

### P - Plan
'''
1. Run the algo
2. Try removing different values from the list
3. Try edge cases like the first or last node
4. Check "off by one errors" in things like lengths, .next, + or - 1
5. Use the scientific method and only change one variable at a time and then test
6. Use the step through debugger
7. Add print statements
'''

# 3. Translate each sub-problem into pseudocode:
'''
while curr:
# BUG = while curr.next: 
# if we use the BUG code from the previous line we will not be able to check
# the last node. 
'''

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

# Function with a bug!
def remove_by_value(head, val):
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current: #BUG - original while loop was "while current.next:"
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

'''
Example Usage:
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3

Example Output:
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4
'''
head = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_by_value(head, 3))


'''
Example Usage:
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 4

Example Output:
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3
'''
head = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_by_value(head, 4))