#####################################
# PROBLEM 2: Convert to Linked List
#####################################

# A linked list is a new data type that, similar to a normal list or array, 
# allows us to store pieces of data sequentially. The difference between a 
# linked list and a normal list lies in how each element is stored in a 
# computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent 
# memory locations according to the order they appear in the list. If we 
# know where the first element of the list is stored, it’s really easy to 
# find any other element in the list.

# In a linked list, the individual elements called nodes are not stored in 
# sequential memory locations. Each node may be stored in an unrelated memory 
# location. To connect nodes together into a sequential list, each node stores 
# a reference or pointer to the next node in the list.

# Using the provided Node class below, create the normal Python list 
# ["Jigglypuff", "Wigglytuff"] as a linked list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How many objects are instantiated in this problem?
    # When creating a new object, what attributes must be specified?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create an object called node_1 and set it equal to Node with "Jigglypuff" as an attribute
    # create an object called node_2 and set it equal to Node with "Wigglytuff" as an attribute
    # set node_1's next attribute equal to node_2

# 3. Translate each sub-problem into pseudocode:
    # node_1 = Node(<name>)
    # node_2 = Node(<name)
    # node_1.next = node_2

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2
		
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)