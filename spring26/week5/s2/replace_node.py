##########################
# PROBLEM 5: REPLACE NODE
##########################

# Using the Node class, write a function ll_replace() that 
# updates in place every node whose value == original to 
# have value = replacement. The function returns None.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is the space complexity of this kind of algorithm? 
    # What is the time complexity?
    # What is the to_string function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Iterate through the linked list with a while loop
    # if the current node's value is equal to the original, update the value to replacement

# 3. Translate each sub-problem into pseudocode:
    # current = head
    # while current:
        # if current.value is equal to original paramater
            # current.value equals replacement parameter
        # current = current.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	current = head
	while current:
		if current.value == original:
			current.value = replacement
		current = current.next
 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
print(to_string(head))