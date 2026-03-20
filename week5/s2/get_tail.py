######################
# PROBLEM 4: GET TAIL
######################

# Write a function get_tail() that takes in the head of a 
# linked list as a parameter.

# Return the value of the tail. If the list is empty, 
# return None.

# Note: The "tail" of a list is the last element in the 
# linked list. Equivalent to lst[-1] in a normal list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of loop is best to iterate through nodes in a linked list?
    # How do we return a specific attribute of a node

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a variable current = head
    # create a while loop that keeps iterating while current.next is equal to True
    # in while loop, set current equal to current's next node
    # outside the while loop (when there is no more next node), return the current node's value

# 3. Translate each sub-problem into pseudocode:
    # def get_tail(head):
        # current = head
        # while current has next node:
            # current = the next node
        # return current.value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	current = head
	while current.next:
		current = current.next
	return current.value

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3