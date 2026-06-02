class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	current = head
	node_list = []
	count = n
	while count > 0 and current:
		node_list.append(current.value)
		current = current.next
		count -= 1
	return node_list

# linked list: a -> b -> c
a = Node("a", Node("b", Node("c")))
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
j = Node("j", Node("k", Node("l")))
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)