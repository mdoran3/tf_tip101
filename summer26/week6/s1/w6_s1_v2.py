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

#######################
# Problem 2: Find Max #
#######################

'''
Given the head of a linked list where each node 
is an integer value, return the maximum value in 
the linked list.
'''

### U - Understand
#   What should we be keeping track of here?
#   How do we iterate through a linked list?
#   Does Python have any built in functionality that might be useful here?

### P - Plan
'''
1. set head equal to a temp variable
2. set a a max variable and set it equal to negative infinity
3. iterate through the linked list
4. for each node set m equal to the max of the max variable or the value ate curr.value
5. return the max value
'''

# 3. Translate each sub-problem into pseudocode:
'''
func(head):
    curr = head
	maximum = negative infinity
	while curr:
        maximum = max of {maximum} OR {curr's value}
		curr = curr's next node
	return maximum
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def find_max(head):
	curr = head
	m = float("-inf")
	while curr:
		m = max(m, curr.value)
		curr = curr.next
	return m

ll = Node(5, Node(6, Node(7, Node(8))))
print(find_max(ll))
'''
Example Usage:

# Linked List: 5 -> 6 -> 7 -> 8 
# Input: head = 5
Example Output:

# Expected Output: 8
'''


#################################
# Problem 3: Remove First Value #
#################################

'''
The following code attempts to remove the first node 
with a given value from a singly linked list based 
but it contains a bug!

Step 1: Copy this code into your IDE.

Step 2: Create your own test cases to run the code 
against, and use print statements and the stack 
trace to identify and fix the bug so that the function 
correctly removes a node by value from the list.
'''

### U - Understand
#   Whats the first thing we should do when inspecting a bug in the code?
#   What do a lot of errors end up being caused from?

### P - Plan
'''
1. Run the algo
2. Try removing different values from the list
3. Try edge cases like the first or last node
4. Check "off by one errors" in things like lengths, .next, + or - 1
5. Use the scientific method and only change one variable at a time and then test
6. Use the step through debugger
7. Add print statements
'''

# 3. Translate each sub-problem into pseudocode:
'''
while curr:
# BUG = while curr.next: 
# if we use the BUG code from the previous line we will not be able to check
# the last node. 
'''

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

# Function with a bug!
def remove_by_value(head, val):
    # Check if the list is empty
    if head is None:
        return head

    # If the node to be removed is the head of the list
    if head.value == val:
        return head.next

    # Initialize pointers
    current = head.next
    previous = head

    # Traverse the list to find the node to remove
    while current: #BUG - original while loop was "while current.next:"
        if current.value == val:
            previous.next = current.next
            return head
        previous = current
        current = current.next

    # If no node was found with the value `val`, return the original head
    return head

'''
Example Usage:
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 3

Example Output:
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 4
'''
head = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_by_value(head, 3))


'''
Example Usage:
# Input List: 1 -> 2 -> 3 -> 4
# Value to Remove: 4

Example Output:
# Expected Return Value: 1
# Expected Result List: 1 -> 2 -> 3
'''
head = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_by_value(head, 4))