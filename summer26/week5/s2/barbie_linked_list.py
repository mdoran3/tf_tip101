##################################
# Problem 2: Barbie Linked List  #
##################################

'''
A linked list is a new data type that, similar to a normal 
list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies 
in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored 
in adjacent memory locations according to the order they appear 
in the list. If we know where the first element of the list is 
stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not 
stored in sequential memory locations. Each node may be stored 
in an unrelated memory location. To connect nodes together into 
a sequential list, each node stores a reference or pointer to 
the next node in the list.

Using the provided Node class below, recreate the list 
['Barbie', 'President Barbie', 'Weird Barbie', 'Ken'] as a 
linked list.
'''

### U - Understand
# 1. What does each Node store, and how do nodes connect to each other?
#    Each Node holds a `value` (the data) and a `next` pointer to the next Node in the sequence.
#    The last node's `next` is None, marking the end of the list.

# 2. What is the order we need, and how do we link them together?
#    We need: Barbie -> President Barbie -> Weird Barbie -> Ken
#    We create each node separately, then set node_1.next = node_2, node_2.next = node_3, etc.


### P - Plan
# 1. Create node_1 with value "Barbie".
# 2. Create node_2 with value "President Barbie", then set node_1.next = node_2.
# 3. Create node_3 with value "Weird Barbie", then set node_2.next = node_3.
# 4. Create node_4 with value "Ken", then set node_3.next = node_4.
#    node_4.next stays None (default) — it's the tail of the list.

# 3. Translate each sub-problem into pseudocode:
'''
node_1 = Node("Barbie")
node_2 = Node("President Barbie")
node_1.next = node_2

node_3 = Node("Weird Barbie")
node_2.next = node_3

node_4 = Node("Ken")
node_3.next = node_4

# node_4.next is None by default — end of list
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
node_1 = Node("Barbie")
node_2 = Node("President Barbie")
node_1.next = node_2
node_3 = Node("weird Barbie")
node_2.next = node_3
node_4 = Node("Ken")
node_3.next = node_4
		
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

'''
Example Output:

Barbie -> President Barbie
President Barbie -> Weird Barbie
Weird Barbie -> Ken
Ken -> None

Result Linked list: Barbie -> President Barbie -> Weird Barbie -> Ken
'''