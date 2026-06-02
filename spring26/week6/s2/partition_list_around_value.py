#########################################
# PROBLEM 3: PARTITION LIST AROUND VALUE
#########################################

# Given the head of a linked list and a value val, partition 
# a linked list around val such that all nodes with values 
# less than val come before nodes with values greater than
#  or equal to val.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What will the space complexity of this algo be?
    # Since were making a partition, how many lists will we be building?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create two linked lists, one for lesser values and one for greater values
    # creater two pointers, one for each beginning of these new lists
    # iterate through the original linked list and check values
    # compare their values to the val given for the partition parameter
    # add each node to the proper list until original LL is completed iterated through
    # stitch the two lists back together and return it

# 3. Translate each sub-problem into pseudocode:
    # list1 = Node(0)
    # list2 = Node(0)
    # p1 = list1
    # p2 = list2

    # current = head
    # while current:
        # if current.value < val:
            # add node to list1
        # else:
            # add node to list2
    # list1.next = list2
    # return list1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def partition(head, val):
    ll1 = Node(0)
    ll2 = Node(0)

    less = ll1
    greater = ll2

    current = head
    while current:
        if current.value < val:
            new_node = current
            less.next = new_node
            less = new_node
            current = current.next
        else:
            new_node = current
            greater.next = new_node
            greater = new_node
            current = current.next

    greater.next = None
    less.next = ll2.next
    return ll1.next

def print_ll(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next



# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
node1 = Node(1)
node2 = Node(4)
node3 = Node(3)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3

linked_list = partition(node1, 3)
print_ll(linked_list)
