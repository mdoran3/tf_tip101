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