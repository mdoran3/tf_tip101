#########################################################
# Problem 1: Print Level Order Traversal of Binary Tree #
#########################################################

'''
Given the following pseudocode and the root of a binary tree, print 
the level order traversal of it’s nodes’ values (i.e., from left to 
right, level by level).

Evaluate the time complexity of your solution. Define your variables 
and give a rationale as to why you believe your solution has the 
stated time complexity.
'''

### U - Understand
'''
1. What should happen if the tree is empty (root is None)? -> Nothing should
   be printed; the function should just return immediately.
2. Does "level by level, left to right" mean I need to group values by level,
   or is printing them one at a time in the right order enough? -> Printing
   one at a time in the right order is enough, since a queue naturally
   processes nodes in level order if I enqueue children in left-to-right
   order as I dequeue each node.
'''

### P - Plan
'''
1. If the root is None, there's nothing to print, so return early.
2. Create an empty queue (deque) to keep track of nodes waiting to be
   processed.
3. Add the root node to the queue to start.
4. While the queue is not empty:
   a. Remove the node at the front of the queue (FIFO order preserves level
      order).
   b. Print that node's value.
   c. If it has a left child, add it to the back of the queue.
   d. If it has a right child, add it to the back of the queue.
5. Because children are enqueued left-before-right and the queue is FIFO,
   all nodes at one level are printed before any node at the next level.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION print_by_level(root):
    IF root is None:
        RETURN

    dq = empty queue
    ADD root TO dq

    WHILE dq is not empty:
        popped_node = REMOVE FRONT of dq
        PRINT popped_node.val
        IF popped_node.left is not None:
            ADD popped_node.left TO dq
        IF popped_node.right is not None:
            ADD popped_node.right TO dq
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque # This is a popular library used for queues

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_by_level(root):
    # If the tree is empty:
    # return
    if not root:
        return 

    # Create an empty queue using deque
    dq = deque()

    # Add the root to the queue
    dq.append(root)

    # While the queue is not empty:
    while dq:
    # Pop the next node off the queue (pop from the left side!)
        popped_node = dq.popleft()
    # Print the popped node
        print(popped_node.val)
    # Add each of the popped node's children to the end of the queue
        if popped_node.left:
            dq.append(popped_node.left)
        if popped_node.right:
            dq.append(popped_node.right)

#####################
####### TESTS #######
#####################
'''
Example Usage:

Example Input Tree

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: (Printed)
4
2
6
1
3
Explanation: 
Level 1: Node 4
Level 2 (left to right): Node 2, Node 6
Level 3 (left to right): Node 1, Node 3
'''

n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, left=n1, right=n3)
n6 = TreeNode(6)
root = TreeNode(4, left=n2, right=n6)

print_by_level(root)