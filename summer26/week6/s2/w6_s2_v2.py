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


####################################################
# Problem 2: Collect Nodes in Cycle in Linked List #
####################################################

'''
Given the head of a linked list, return the elements of
any cycle in the linked list as a list.
'''

### U - Understand
#   What types of data structures might be involved in this problem?
#   Do we need to keep track of any frequencies?

### P - Plan
'''
1. Traverse the linked list from the head, keeping a dictionary (freq)
   that maps each node's value to how many times it has been visited.
2. Also keep a list (nodes) to collect the values that are part of a cycle.
3. For each node visited:
   - If its value is not yet in freq, add it with a count of 1 and move on.
   - If its value is already in freq, it means we've looped back to a
     node we've seen before, so it must be part of a cycle:
       - Add its value to nodes if it isn't already there.
       - Increment its count in freq.
       - If its count reaches 3, we've gone around the cycle enough
         times to have collected all cycle nodes, so stop traversing.
4. Return the nodes list. If there is no cycle, curr will eventually
   become None and the loop ends naturally, returning an empty list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN collect_cycle_nodes(head)
    DECLARE freq AS empty map of value -> count (a dictionary)
    DECLARE nodes AS empty list
    SET current TO head

    WHILE current is not null DO
        IF freq does not contain current's value THEN
            SET freq[current's value] TO 1
            SET current TO current's next node
        ELSE
            IF nodes does not contain current's value THEN
                APPEND current's value TO nodes
            END IF
            INCREMENT freq[current's value]
            IF freq[current's value] EQUALS 3 THEN
                BREAK
            END IF
            SET current TO current's next node
        END IF
    END WHILE

    RETURN nodes
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_cycle_nodes(head):
    freq = {}
    nodes = []
    curr = head
    while curr:
        if curr.value not in freq:
            freq[curr.value] = 1
            curr = curr.next
        else:
            if curr.value not in nodes:
                nodes.append(curr.value) 
            freq[curr.value] += 1
            if freq[curr.value] == 3:
                break
            curr = curr.next
    return nodes

########################################
# num1 -> num2 -> num3 -> num4 -> num2 #
########################################
num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)

num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

lst = collect_cycle_nodes(num1)
print(lst)

################################
# var1 -> var2 -> var3 -> var4 #
################################
var1 = Node("a")
var2 = Node("b")
var3 = Node("c")
var4 = Node("d")

lst2 = collect_cycle_nodes(var1)
print(lst2)

'''
Example Output:

[num2, num3, num4]
[]
'''


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