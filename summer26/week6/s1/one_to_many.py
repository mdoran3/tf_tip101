##########################
# Problem 1: One to Many #
##########################

'''
The assignment statement to the head variable below creates the 
linked list Mario -> Luigi -> Wario. Break apart the assignment 
statement into multiple lines with one call to the Node 
constructor per line to recreate the list.
'''

### U - Understand
#   How can we create a node object?
#   What connects them together? 
#   Describe how linked list are held in memory.
#   Bonus: Are you able to write a function that prints the linked list?

### P - Plan
'''
1. Create Mario object
2. Create Lugi object
3. Create Wario object
4. Connect Mario object to Luigi object
5. Connect Luigi object to Wario object
'''

# 3. Translate each sub-problem into pseudocode:
'''
obj1 = Node("Name1)
obj2 = Node("Name2)
obj3 = Node("Name3)

obj1.next = obj2
obj2.next = obj3
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def print_ll(head):
	curr = head
	str = ""
	while curr.next:
		str = str + curr.value + " -> "
		curr = curr.next
	print(f"{str}{curr.value}")

# head = Node("Mario", Node("Luigi", Node("Wario")))
mario = Node("Mario")
luigi = Node("Luigi")
wario = Node("Wario")
mario.next = luigi
luigi.next = wario

head = mario
print_ll(head)