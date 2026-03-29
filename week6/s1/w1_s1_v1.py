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


##############################
# PROBLEM 2: FIND FREQUENCY
##############################

# Given the head of a linked list and a value val, 
# return the frequency of val in the list. Evaluate 
# the time and space complexity of your solution. 
# Define your variables and provide a rationale for 
# why you believe your solution has the stated time 
# and space complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of loop should we use to iterate through the linked list?
    # How do we keep track of the frequency?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set head equal to current
    # set a count variable equal to zero
    # Start a while loop while a current node is available
        # if the value of the current node equals the value parameter
            # increment count by 1
        # make current equal to the next node
    # return count

# 3. Translate each sub-problem into pseudocode:
    # current = head
    # freq = 0
    # while current
        # if current value == val
            # freq = freq + 1
        # current = next node
    # return freq

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	current = head
	count = 0
	while current:
		if current.value == val:
			count += 1
		current = current.next
	return count

ll = Node(3, Node(1, Node(2, Node(1))))
print(count_element(ll, 1))


#########################
# PROBLEM 3: REMOVE TAIL
#########################

# The following code attempts to remove the tail 
# of a singly linked list. However, it has a bug!

# Step 1: Copy this code into your IDE.

# Step 2: Create your own test cases to run the
# code against, and use print statements and the 
# stack trace to identify and fix the bug so that 
# the function correctly removes the tail of the 
# list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is an off by one error?
    # What are a few ways to debug code to get to a solution?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # run a debugger and step through problem
    # check for off by one errors and adjust 
    # add print statements

# 3. Translate each sub-problem into pseudocode:
    # while current.next.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next        

     
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

ll = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_tail(ll))


##############################
# PROBLEM 4: FIND THE MIDDLE
##############################

# A variation of the two-pointer technique introduced in Unit 4 
# is to have a slow and a fast pointer that increment at different 
# rates. Given the head of a linked list, use the slow-fast pointer
# technique to find the middle node of a linked list. If there are 
# two middle nodes, return the second middle node.

# Evaluate the time and space complexity of your solution. Define your 
# variables and provide a rationale for why you believe your solution 
# has the stated time and space complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can a slow and fast pointer, on a high level, find a middle?
    # In what case will there be two middle nodes?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set the slow and fast pointer equal to head
    # while fast and fast.next exist
        # increment the slow pointer by 1
        # increment the fast pointer by 2
    # the value at slow should be at center now, retrn it

# 3. Translate each sub-problem into pseudocode:
    # slow = head
    # fast = head
    # while fast and fast.next
        # slow = slow.next
        # fast = fast.next
    # return slow value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

ll = Node(1, Node(2, Node(3)))
print(find_middle_element(ll))

ll2 = Node(1, Node(2, Node(3, Node(4))))
print(find_middle_element(ll2))