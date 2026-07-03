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