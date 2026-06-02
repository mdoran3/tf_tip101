# Write a function ll_insert() that takes in a head of a l
# inked list, a value val, and an index i as parameters.

# The function should insert a new Node with value val at 
# index i of the linked list, then return the head of the 
# linked list.

# If i is greater than the length of the list, insert the 
# new node at the end of the list.
# Hint: Linked lists do not have built-in indices so you 
# will need to track the indices yourself.

# Write a helper function to help you print the new list!

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
	new_node = Node(val)
	if i == 0:
		new_node.next = head
		return new_node
	current = head
	index = 0
	while current.next and index < i - 1:
		current = current.next
		index += 1
	new_node.next = current.next
	current.next = new_node
	return head

def print_list(head):
	values = []
	while head:
		values.append(str(head.value))
		head = head.next
	print(" -> ".join(values))

# linked list: 3 -> 8 -> 12 -> 9
head = Node(3, Node(8, Node(12, Node(9))))
print_list(head)

ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9
print_list(head)