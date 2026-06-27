#################################
# Problem 3: Insert Value First #
#################################

'''
Using the Node class, write a function add_first() that takes 
in the head of a linked list and a value object val as parameters.

The function should insert a new Node object with value val as 
the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the 
linked list. Equivalent to lst[0] of a normal list.
'''

### U - Understand
# 1. What should be returned — the new node itself, or the full updated list?
# 2. What should happen if the head is None (empty list) — does val become the only node?

### P - Plan
# 1. Create a new Node with value val
# 2. Set the new node's next pointer to the current head
# 3. Return the new node as the new head

# 3. Translate each sub-problem into pseudocode:
'''
new_node = Node(val)
new_node.next = head
return new_node
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
			
def add_first(head, val):
	if not head:
		node = Node(val)
		return node
	else:
		new_node = Node(val, head)
		return new_node

def print_ll(ll):
	lst_str = ""
	head = ll
	while head:
		lst_str = lst_str + head.value + " -> "
		head = head.next
	return lst_str

node1 = Node("A")
node2 = Node("B")
node1.next = node2
node3 = Node("C")
node2.next = node3

ll = add_first(node1, "0")
print(print_ll(ll))

'''
Example Usage:

# Linked List: A -> B -> C
new_list = add_first(node_a, 0)
# New List: 0 -> A -> B -> C
'''