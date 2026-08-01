##################################
# Problem 2: Reverse_Linked_List #
##################################

'''
Given the head of a singly linked list, reverse the list, 
and return the head of the reversed list.
'''

### U - Understand
'''
1. What does "reversing" the list actually mean in terms of each node's
   `next` pointer, rather than just the order values are printed in?
2. What should be returned as the new head, and what happens to the
   original head node's `next` pointer once the list is reversed?
'''

### P - Plan
'''
1. Walk through the list one node at a time, keeping track of the
   previously visited node (starting with none, since the new tail's
   next should point to nothing).
2. At each node, save its next node before overwriting it, then point
   the current node's next back at the previous node.
3. Advance both the "previous" and "current" pointers forward, and once
   the current pointer runs off the end of the list, the last node
   visited is the new head - return it.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set prev = None
    set curr = head

    WHILE curr is not None:
        set next_node = curr.next
        set curr.next = prev
        set prev = curr
        set curr = next_node

    RETURN prev
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
	prev = None
	curr = head
	while curr is not None:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	return prev
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input List: 1 -> 2 -> 3 -> 4
Input: head = 3, val = 1
Expected Return Value: 4
Expected Result List: 4 -> 3 -> 2 -> 1
'''
head = Node(1, Node(2, Node(3, Node(4))))
new_head = reverse(head)

result = []
node = new_head
while node is not None:
	result.append(node.value)
	node = node.next
print(result)