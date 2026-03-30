###################################################
# PROBLEM 2: FIND LAST NODE IN A LINKED LIST CYCLE
###################################################

# Given the head of a singly linked list, write a function that 
# returns the last node in the cycle. If there is no cycle in
# the linked list, return None.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What type of loop should be used in this problem?
    # What data structure will help us keep track of nodes?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a set called seend to store nodes in
    # create current pointer from head
    # start while loop for while current
    # if current isn't in the set, add it in and increment current
    # else if current is in the seen set, return the node
    # return None otherwise

# 3. Translate each sub-problem into pseudocode:
    # seen = set()
    # curr = head
    # while curr
        # if currn is not in seen:
            # add it
            # increment curr
        # else:
            # return node
    # return None

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_last_node_in_cycle(head):
    if head is None or head.next is None:
        return None
    
    seen = set()
    current = head
    while current:
        if current not in seen:
            seen.add(current)
            current = current.next
        else:
            return current
    return None
    
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

node = find_last_node_in_cycle(num1)
print(node.value)