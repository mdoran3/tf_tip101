##################################
# PROBLEM 1: NESTED CONSTRUCTORS
##################################

# Step 1: Copy the following code into your IDE.

# Step 2: Add a line of code (outside of the class) to create 
# the linked list 4 -> 3 -> 2 in a single assignment statement.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is a constructor?
    # How can we nest new objects and create a LL in one line?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a variable for a linked list
    # Instantiate a Node object with its value as the first param, and then another 
        # Node object as the second param that will have its own value and on and on.

# 3. Translate each sub-problem into pseudocode:
    # linked_list = Node(num, Node(num, Node(num)))

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
ll = Node(4, Node(3, Node(2)))