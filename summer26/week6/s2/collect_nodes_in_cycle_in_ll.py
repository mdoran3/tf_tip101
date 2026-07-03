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