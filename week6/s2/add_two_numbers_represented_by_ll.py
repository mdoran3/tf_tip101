###########################################################
# PROBLEM 5: ADD TWO NUMBERS REPRESENTED BY A LINKED LIST
###########################################################

# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their nodes 
# contains a single digit. Add the two numbers and return the sum as a linked list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How do we cast from int to string and vice versa?
    # How many pointers will be used in this problem most likely?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create two new lists
    # create pointers for each
    # while loop while both pointers exist
        # append value of each node from each list to respective lists
        # increment pointers
    # reverse each list
    # convert each list to a string
    # cast each string to an int and add them together for a result number
    # cast this number back to a string
    # reverse this string
    # Create head node of new list
    # create a pointer for it as well
    # iterate through each char in this string
    # convert each char to an int and save it as a variable
    # create a new node with each new int and have the new linkedlist pointer.next point to it
    # increment the new linkedlist pointer
    # return the new linkedlist.next

# 3. Translate each sub-problem into pseudocode:
    # list1, list2 = []
    # p1 = head_a
    # p2 = head_b
    # while p1 and p2
        # list1.append(str(p1.value))
        # list2.append(str(p2.value))
        # p1 & p2 = p1.next & p2.next
    # list1.rev & list2.rev
    # str(list1) and str(list2) ===> str1 and str2
    # new_num = int(str1) + int(str2)
    # new_num_str = str(new_num) & reversed()
    # ll = Node(0)
    # ll_poiner = ll
    # for char in new_num_str:
        # num = int(char)
        # new_node = Node(num)
        # ll_pointer.next = new_node
        # ll_pointer = ll_pointer.next
    # return ll.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_two_numbers(head_a, head_b):
    no1 = []
    no2 = []

    p1 = head_a
    p2 = head_b

    while p1 and p2:
        no1.append(str(p1.value))
        no2.append(str(p2.value))
        p1 = p1.next
        p2 = p2.next

    no1_rev = no1[::-1]
    no2_rev = no2[::-1]
    no1_i = "".join(no1_rev)
    no2_i = "".join(no2_rev)
    new_num = int(no1_i) + int(no2_i)
    num_str = str(new_num)
    new_str_rev = reversed(num_str)
    ll = Node(0)
    ll_ptr = ll

    for char in new_str_rev:
        num = int(char)
        ll_ptr.next = Node(num)
        ll_ptr = ll_ptr.next
    return ll.next

def print_ll(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# list 1: 2 -> 4 -> 3 (342)
# list 2: 5 -> 6 -> 4 (465)
# head_a = 2, head_b = 5
node1 = Node(2)
node2 = Node(4)
node3 = Node(3)
node1.next = node2
node2.next = node3

node4 = Node(5)
node5 = Node(6)
node6 = Node(4)
node4.next = node5
node5.next = node6

sum = add_two_numbers(node1, node4)
print_ll(sum)