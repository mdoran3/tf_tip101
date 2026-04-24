############################
# PROBLEM 3: SHUFFLE MERGE #
############################

# Given the heads of two singly linked lists of integers, 
# merge their nodes to make one list, taking nodes alternately 
# between the two lists. If either list runs out of elements 
# before the other, all nodes from the list with remaining 
# nodes should be appended onto the end of the merged list. 
# Return the head of the merged list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we iterate through and alternate between lists?
    # Do we need to create a new list? What is the space complexity? 

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a new linked list by initializing a node and naming it.
    # make a copy of it to iterate with
    # use a while loop to iterate while either of the lists are still valid
    # take the head of one list and create a new ListNode and set your new LL .next to this node.
        # decrement up in that LL and the new LL
    # Repeat this for the next list to be joined
    # return the non copied version of the list created and return its head as its .next

# 3. Translate each sub-problem into pseudocode:
    # temp = ListNode(0)
    # current = temp
    # while head_a or head_b:
    #     if head_a:
    #         current.next = ListNode(head_a.val)
    #         current = current.next
    #         head_a = head_a.next
    #     if head_b:
    #         current.next = ListNode(head_b.val)
    #         current = current.next
    #         head_b = head_b.next
    # return temp.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class ListNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def print_linked_list(head):
	values = []
	while head:
		values.append(str(head.val))
		head = head.next
	print(" -> ".join(values))

def shuffle_merge(head_a, head_b):
	temp = ListNode(0)
	shuffled = temp

	while head_a or head_b:
		if head_a:
			node_a = ListNode(head_a.val)
			shuffled.next = node_a
			shuffled = shuffled.next
			head_a = head_a.next
		if head_b:
			node_b = ListNode(head_b.val)
			shuffled.next = node_b
			shuffled = shuffled.next
			head_b = head_b.next
	return temp.next

# Test 1: List 1: 1 -> 2 -> 3, List 2: 4 -> 5 -> 6
# Expected: 1 -> 4 -> 2 -> 5 -> 3 -> 6
a1 = ListNode(1, ListNode(2, ListNode(3)))
b1 = ListNode(4, ListNode(5, ListNode(6)))
print_linked_list(shuffle_merge(a1, b1))

# Test 2: List 1: 1 -> 2 -> 3, List 2: 4
# Expected: 1 -> 4 -> 2 -> 3
a2 = ListNode(1, ListNode(2, ListNode(3)))
b2 = ListNode(4)
print_linked_list(shuffle_merge(a2, b2))