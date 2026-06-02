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