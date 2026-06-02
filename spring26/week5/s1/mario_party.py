class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
node_1 = Node("Mario")
node_2 = Node("Luigi")
node_3 = Node("Wario")
node_4 = Node("Toad")
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
		
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)