#######################
# PROBLEM 3: Add First
#######################

# Write a function add_first() that takes in a head of a 
# linked list and a new_node from the Node class as parameters.

# It should insert new_node as the new head of the linked_list. 
# The function returns new_node.

# Note: The "head" of a linked list is the first element in 
# the linked list. Equivalent to lst[0] of a normal list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How does inserting a node differ from adding to an array?
    # What is the head of a linked list?
    # Are linked list coniguous blocks in memory?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Take in head and new_node as parameters
    # set new_node's next value to head
    # now technically new_node will be head 
    # return new_node

# 3. Translate each sub-problem into pseudocode:
    # new_node.next = head
    # return new_node

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node

# Using the Linked List from Problem 2
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)