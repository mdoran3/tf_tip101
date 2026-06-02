##########################################
# PROBLEM 1: DETECT CIRCULAR LINKED LIST
##########################################

# A circular linked list is a linked list where the tail node points
# at the head node. Given the head of a linked list, write a function 
# is_circular() that returns True if the linked list is circular and 
# False otherwise.

# Note: a circular list is more than just a cycle - specifically 
# connecting the first and last nodes.

# Evaluate the time and space complexity of your solution. Define 
# your variables and provide a rationale for why you believe your 
# solution has the stated time and space complexity.


### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What makes a linked list circular?
    # What should we be comparing in the LL during our iterations?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set currnet equal to head.next in order to compare curent and head
    # Use a while loop while current and current not equal to head
    # Iterate current to the next node
    # outside while loop return current == to head (T or F)

# 3. Translate each sub-problem into pseudocode:
    # current = head.next
    # while current exists and current does not equal head
        # current = current.next
    # return current equals head (True of False return)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    current = head.next
    while current and current != head:
        current = current.next
    return current == head

# num1 -> num2 -> num3 -> num1
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
print(is_circular(num1))

# var1 -> var2 -> var3
var1 = Node(1)
var2 = Node(2)
var3 = Node(3)
var1.next = var2
var2.next = var3
print(is_circular(var1))


###################################################
# PROBLEM 2: FIND LAST NODE IN A LINKED LIST CYCLE
###################################################

# Given the head of a singly linked list, write a function that 
# returns the last node in the cycle. If there is no cycle in
# the linked list, return None.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What type of loop should be used in this problem?
    # What data structure will help us keep track of nodes?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a set called seend to store nodes in
    # create current pointer from head
    # start while loop for while current
    # if current isn't in the set, add it in and increment current
    # else if current is in the seen set, return the node
    # return None otherwise

# 3. Translate each sub-problem into pseudocode:
    # seen = set()
    # curr = head
    # while curr
        # if currn is not in seen:
            # add it
            # increment curr
        # else:
            # return node
    # return None

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_last_node_in_cycle(head):
    if head is None or head.next is None:
        return None
    
    seen = set()
    current = head
    while current:
        if current not in seen:
            seen.add(current)
            current = current.next
        else:
            return current
    return None
    
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

node = find_last_node_in_cycle(num1)
print(node.value)


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

###################################################################
# PROBLEM 4: CONVERT BINARY NUMBER IN A LINKED LIST TO AN INTEGER
###################################################################

# You are given the head of a linked list. Each value in the linked list 
# is either 0 or 1, and the entire linked list represents a binary number. 
# Return an integer that is the decimal value of the number represented by 
# the linked list. The most significant bit is at the head of the linked list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How do we convert binary to decimal?
    # Should we use other data structures to store information for calculations?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a list for binary digits
    # create a current pointer
    # iterate LL while current
    # append each node value to the binary digit list
    # move pointer up a node
    # create a number variable to store the final number
    # create and i variable for iterations
    # get the length of the binary list
    # set a while loop while i less than length
    # pop() digit of stack of binary
    # if the popped number is equal to 1, add 2^ith to num
    # increment i
    # return number

# 3. Translate each sub-problem into pseudocode:
    # stack = []
    # current = head
    # while current:
        # stack.append(current.value)
        # current = current.next
    # num = 0
    # length = len(stack)
    # i = 0
    # while i < length:
        # digi = stack.pop()
        # if digi == 1:
            # num += 2**i
        # i += 1
    # return num

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def binary_to_int(head):
    binaries = []
    current = head
    while current:
        binaries.append(current.value)
        current = current.next
    num = 0
    i = 0
    length = len(binaries)
    while i < length:
        bi = binaries.pop()
        if bi == 1:
            num += 2**i
        i += 1
    return num
    

# 1 -> 0 -> 1
num3 = Node(1)
num2 = Node(0, num3)
num1 = Node(1, num2)   # head of the list

int_num = binary_to_int(num1)
# 101 in binary is 5
print(int_num)  # Output: 5



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