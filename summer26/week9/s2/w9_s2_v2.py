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



#########################################################
# Problem 2: Sum of Node Values by Level in Binary Tree #
#########################################################

'''
Given the root of a binary tree, return a list of the sums of 
node values in each level in the binary tree.

Evaluate the time complexity of your solution. Define your variables 
and give a rationale as to why you believe your solution has the 
stated time complexity.
'''

### U - Understand
'''
1. What should be returned for an empty tree (root is None)? -> An empty
   list, since there are no levels to sum.
2. Do I need to know how many levels there are in advance, or can I discover
   that as I go? -> I can discover it as I go, by processing the tree one
   level at a time and adding a new sum to the result list for each level.
'''

### P - Plan
'''
1. If the root is None, return an empty list right away.
2. Create an empty queue (deque) and add the root to it, plus an empty
   results list.
3. While the queue is not empty, process one full level at a time:
   a. Record how many nodes are currently in the queue (that's the size of
      this level).
   b. Initialize a running sum of 0 for this level.
   c. Remove that many nodes from the front of the queue, adding each
      node's value to the level sum, and enqueueing each node's children
      (left then right) for the next level.
   d. Append the level sum to the results list.
4. Once the queue is empty, every level has been processed; return the
   results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION level_sum(root):
    IF root is None:
        RETURN empty list

    dq = empty queue
    ADD root TO dq
    sums = empty list

    WHILE dq is not empty:
        level_size = LENGTH of dq
        level_total = 0
        REPEAT level_size TIMES:
            node = REMOVE FRONT of dq
            level_total = level_total + node.val
            IF node.left is not None:
                ADD node.left TO dq
            IF node.right is not None:
                ADD node.right TO dq
        ADD level_total TO sums

    RETURN sums
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def level_sum(root):
    if not root:
        return []

    dq = deque([root])
    sums = []

    while dq:
        level_size = len(dq)
        level_total = 0
        for _ in range(level_size):
            node = dq.popleft()
            level_total += node.val
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        sums.append(level_total)

    return sums


#####################
####### TESTS #######
#####################
'''
Example Input Tree

      4
     / \
    2   6
   / \
  1   3

Example Input: root = 4
Expected Output: [4, 8, 4]
Explanation:
Level 1: 4 -> sum = 4
Level 2: 2 + 6 -> sum = 8
Level 3: 1 + 3 -> sum = 4
'''

n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, left=n1, right=n3)
n6 = TreeNode(6)
root = TreeNode(4, left=n2, right=n6)

print(level_sum(root))



########################################################
# Problem 3: Maximum Nodes at Any Level in Binary Tree #
########################################################

'''
Given the root of a binary tree, return the maximum number of 
nodes in any level of the binary tree.

Evaluate the time complexity of your solution. Define your 
variables and give a rationale as to why you believe your solution 
has the stated time complexity.
'''

### U - Understand
'''
1. What should be returned for an empty tree (root is None)? -> 0, since
   there are no levels and therefore no nodes at any level.
2. Do I need the sums or values of the nodes, or just how many nodes are at
   each level? -> Just the count of nodes at each level; I only need to
   track the size of each level as I traverse and keep the largest one.
'''

### P - Plan
'''
1. If the root is None, return 0 right away.
2. Create an empty queue (deque) and add the root to it, plus a variable to
   track the maximum level size seen so far (start at 0).
3. While the queue is not empty, process one full level at a time:
   a. Record how many nodes are currently in the queue (that's the size of
      this level).
   b. Update the maximum if this level's size is larger than what's been
      seen so far.
   c. Remove that many nodes from the front of the queue, enqueueing each
      node's children (left then right) for the next level.
4. Once the queue is empty, every level has been processed; return the
   maximum level size found.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION level_max(root):
    IF root is None:
        RETURN 0

    dq = empty queue
    ADD root TO dq
    max_count = 0

    WHILE dq is not empty:
        level_size = LENGTH of dq
        max_count = MAX(max_count, level_size)
        REPEAT level_size TIMES:
            node = REMOVE FRONT of dq
            IF node.left is not None:
                ADD node.left TO dq
            IF node.right is not None:
                ADD node.right TO dq

    RETURN max_count
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_max(root):
    if not root:
        return 0

    dq = deque([root])
    max_count = 0

    while dq:
        level_size = len(dq)
        max_count = max(max_count, level_size)
        for _ in range(level_size):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

    return max_count

#####################
####### TESTS #######
#####################
'''
Example Usage:

Example Input Tree #1:

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: 2
Explanation: Levels 2 & 3 have 2 nodes each. 

Example Input Tree #2:

       1
      / \
     /   \
    2     3
   / \   / \ 
  4   5 6   7

Example Input: root = 1
Expected Output: 4
Explanation: Level 3 has 4 nodes, the most of any level
'''

# Tree #1
n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, left=n1, right=n3)
n6 = TreeNode(6)
tree1 = TreeNode(4, left=n2, right=n6)

# Tree #2
n4 = TreeNode(4)
n5 = TreeNode(5)
n2b = TreeNode(2, left=n4, right=n5)
n6b = TreeNode(6)
n7 = TreeNode(7)
n3b = TreeNode(3, left=n6b, right=n7)
tree2 = TreeNode(1, left=n2b, right=n3b)

print(level_max(tree1))
print(level_max(tree2))