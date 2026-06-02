class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	string = ""
	current = head
	while current.next:
		string = f"{string} {current.value} -> "
		current = current.next
	string = f"{string} {current.value}"
	print(string)

a = Node("a", Node("b", Node("c", Node("d", Node("e")))))
print_linked_list(a)