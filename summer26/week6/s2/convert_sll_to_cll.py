###################################################################
# Problem 1: Convert Singly Linked List to a Circular Linked List #
###################################################################

'''
A circular linked list is a linked list where the tail node points at 
the head node. Write a function that transforms a singly linked list 
into a circular linked list. Return the head of the linked list. 
Evaluate the time and space complexity of your solution. Define your 
variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.
'''

### U - Understand
#   How do we find the tail of a linked list?
#   How do we connect the tail to the head?

### P - Plan
'''
1. set head to a variable like curr
2. set while loop while there is a next node
3. step to the next node
4. outside the while loop, set curr's next point to head
5. return head
'''

# 3. Translate each sub-problem into pseudocode:
'''
func(head):
    curr = head
    while curr's next ndoe exists:
        curr = curr's next node
    curr's next = head
    return head
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def make_circular(head):
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = head
    return head

def print_ll(head, limit=10):
    curr = head
    count = 0
    values = []
    while curr and count < limit:
        values.append(str(curr.value))
        curr = curr.next
        count += 1
        if curr is head:
            values.append(f"(back to head: {head.value})")
            break
    print(" -> ".join(values))

'''
Example Usage:

# Input List: num1 -> num2 -> num3
make_circular(num1)
Result Linked List: num1 -> num2 -> num3 -> num1
'''

head = Node(1, Node(2, Node(3,)))
print_ll(make_circular(head))