############################################
# Problem 3: Delete Duplicates Linked List #
############################################

'''
Given the head of a sorted linked list, delete all 
elements that occur more than once in the list (not 
just the duplicates). The resulting list should maintain 
sorted order. Return the head of the linked list.
'''

### U - Understand
#   How do we "remove" an element from a linked list?
#   Do we need to keep track of any additional variables or lists?

### P - Plan
'''
1. Since the list is sorted, any duplicate values will always sit
   next to each other, so we only ever need to compare a node to
   the node right after it.
2. Traverse the list with a single pointer, curr, starting at head.
3. At each step, compare curr's value to curr.next's value:
   - If they are equal, remove curr.next from the list by pointing
     curr.next to curr.next.next. Do NOT advance curr yet, so that
     runs of more than two duplicates in a row keep collapsing.
   - If they are not equal, advance curr to curr.next.
4. Stop once curr.next is None (we've reached the end of the list).
5. Return head.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN delete_dupes(head)
    SET current TO head

    WHILE current's next node is not null DO
        IF current's value EQUALS current's next node's value THEN
            SET current's next TO current's next node's next node
        ELSE
            SET current TO current's next node
        END IF
    END WHILE

    RETURN head
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def delete_dupes(head):
    curr = head
    while curr.next:
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def print_ll(head):
    values = []
    curr = head
    while curr:
        values.append(str(curr.value))
        curr = curr.next
    print(" -> ".join(values))         

'''
Example Input: 1 -> 2 -> 3 -> 3 -> 4 -> 5

Example Output: 1 -> 2 -> 4 -> 5
'''

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5, Node(5, Node(5))))))))
print_ll(delete_dupes(head))