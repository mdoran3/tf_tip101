###################################################
# PROBLEM 1: LEVEL ORDER TRAVERSAL OF BINARY TREE #
###################################################

# Given the following pseudocode and the root of a binary tree, 
# return a list of the level order traversal of it’s nodes’ 
# values (i.e., from left to right, level by level).

# Evaluate the time complexity of your solution. Define your 
# variables and give a rationale as to why you believe your 
# solution has the stated time complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How does a deque work and what is one of its key operations that will be useful here?
    # Why is a while loop effective here?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a list variable for visited nodes and a deque DS
    # if the root is none, just return
    # add root to the deque
    # create a while loop
        # pop from teh left of the deque and save this variable
        # add the popped variable to the visited nodes
        # if popped.left exists add it to the deque
        # if popped.right exists, add it to the deque
    # return the visited nodes list

# 3. Translate each sub-problem into pseudocode:
    # If ther tree is empty, return an empty list
    # create a deque data structure
    # create a list to store the visited nodes in order
    # append the root of the tree to the deque
    # while the deque is not empty
        # popped = popleft() from the deque
        # visited.append(popped)
        # if popped.left
            # deque.append(popped.left)
        # if popped.rigth
            # deque.append(popped.right)
    # return visited
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []

    # Create an empty queue using deque
    dq = deque()

    # Create an empty list to store the explored nodes
    level_nodes = []

    # Add the root to the queue
    dq.append(root)

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    while dq:
        popped_node = dq.popleft()
        level_nodes.append(popped_node.val)

    # Add each of the popped node's children to the end of the queue
        if popped_node.left:
            dq.append(popped_node.left)
        if popped_node.right:
            dq.append(popped_node.right)

    # Return the list of visited nodes
    return level_nodes

# Example Input Tree:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: [4, 2, 6, 1, 3]
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3
bst = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_order(bst))


################################################
# PROBLEM 2: FIND MINIMUM DEPTH OF BINARY TREE #
################################################

# Given the root of a binary tree, return its minimum depth. 
# The minimum depth is the number of nodes along the shortest 
# path from the root down to the nearest leaf node.

# Evaluate the time complexity of your solution. Define your 
# variables and give a rationale as to why you believe your 
# solution has the stated time complexity.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # What should we return if the tree is empty (root is None)?
    # what data structure will we need to import

### P - Plan
# 2. Write out in plain English what you want to do:
#    Use BFS to traverse the tree level by level. For each node we
#    dequeue, check if it is a leaf (no left and no right child).
#    Because BFS explores nodes in order of increasing depth, the
#    first leaf we encounter is guaranteed to be on the shallowest
#    level, so we return its depth immediately.

# 3. Translate each sub-problem into pseudocode:
#    - If root is None, return 0
#    - Initialize a queue with (root, depth=1)
#    - While the queue is not empty:
#        - Dequeue (node, depth)
#        - If node has no left and no right child, return depth
#        - If node has a left child, enqueue (left, depth + 1)
#        - If node has a right child, enqueue (right, depth + 1)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
        
def min_depth(root):
    if root is None:
        return 0
    dq = deque([(root, 1)])
    while dq:
        node, depth = dq.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            dq.append((node.left, depth + 1))
        if node.right:
            dq.append((node.right, depth + 1))

# Example Input Tree #1:

#    3
#   / \
#  9  20
#     / \
#    15  7

# Example Input: root = 3
# Expected Output: 2
# Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

node15 = TreeNode(15)
node7 = TreeNode(7)
node9 = TreeNode(9)
node20 = TreeNode(20, node15, node7)
root1 = TreeNode(3, node9, node20)
print(min_depth(root1))

# Example Input Tree #2:

#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6

# Example Input: root = 2
# Expected Output: 5
# Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
# Number of nodes in path is 5.

node6 = TreeNode(6)
node5 = TreeNode(5, None, node6)
node4 = TreeNode(4, None, node5)
node3 = TreeNode(3, None, node4)
root2 = TreeNode(2, None, node3)
print(min_depth(root2))


###################################################
# PROBLEM 3: LEVEL ORDER TRAVERSAL OF BINARY TREE #
###################################################

# Given the root of a binary tree, return the difference between 
# the sum of all node values in odd levels and sum of all node 
# values in even levels.

# Evaluate the time complexity of your solution. Define your 
# variables and give a rationale as to why you believe your 
# solution has the stated time complexity.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Is the root considered level 1 (odd), so even levels are its children?
    # What should we return if the tree is empty?

### P - Plan
# 2. Write out in plain English what you want to do:
#    Use BFS to traverse the tree level by level. Track each node's depth
#    as we enqueue it. For each node we dequeue, add its value to the odd
#    sum or even sum depending on whether its depth is odd or even.
#    Return odd sum minus even sum.

# 3. Translate each sub-problem into pseudocode:
#    if root is None, return 0
#    initialize odd = 0, even = 0
#    initialize deque with (root, depth=1)
#    while deque is not empty:
#        pop (node, depth) from front
#        if depth is even: even += node.val
#        else: odd += node.val
#        if node.left: enqueue (node.left, depth + 1)
#        if node.right: enqueue (node.right, depth + 1)
#    return odd - even

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_difference(root):
    if root is None:
        return 0
    even = 0
    odd = 0
    dq = deque([(root, 1)])
    while dq:
        node, depth = dq.popleft()
        if depth % 2 == 0:
            even += node.val
        else:
            odd += node.val
        if node.left:
            dq.append((node.left, depth + 1))
        if node.right:
            dq.append((node.right, depth + 1))
    return odd - even
        
# Example Input Tree
#           6
#          / \
#         3   8
#        /   / \
#       5   4   2
#          / \   \
#         1   7   3
# Expected Output: -5
# Explanation:
# Odd level sum: 6 + 5 + 4 + 2 = 17
# Even level sum: 3 + 8 + 1 + 7 + 3 = 22
# Odd level sum - even level sum: 17 - 22 = -5

node1 = TreeNode(1)
node7 = TreeNode(7)
node3_leaf = TreeNode(3)
node5 = TreeNode(5)
node4 = TreeNode(4, node1, node7)
node2 = TreeNode(2, None, node3_leaf)
node3 = TreeNode(3, node5)
node8 = TreeNode(8, node4, node2)
root = TreeNode(6, node3, node8)
print(level_difference(root))

#####################################################################
# PROBLEM 4: LEVEL ORDER TRAVERSAL OF BINARY TREE WITH NESTED LISTS #
#####################################################################

# Given the root of a binary tree, write a function level_order() that returns 
# the level order traversal of its nodes’ values (i.e., from left to right, 
# level by level). level_order() should return a list of lists, where each 
# inner list contains the node values of a single level in the tree.

# Evaluate the time complexity of your solution. Define your variables and 
# give a rationale as to why you believe your solution has the stated time 
# complexity.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # How can we sure we are only dealing with one level at a time i the while loop?
    # Should we return an empty list if the root is None, or raise an error?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use BFS with a queue. Start by adding the root to the queue.
# On each iteration, snapshot the current queue size so we know how many nodes
# belong to the current level. Process exactly that many nodes, collecting their
# values into a sub-list, and enqueue their children. Append the sub-list to the
# result. Repeat until the queue is empty, then return the result.

# 3. Translate each sub-problem into pseudocode:
# if root is None: return []
# queue = deque([root])
# result = []
# while queue is not empty:
#     level_size = len(queue)
#     current_level = []
#     for i in range(level_size):
#         node = queue.popleft()
#         current_level.append(node.val)
#         if node.left:  queue.append(node.left)
#         if node.right: queue.append(node.right)
#     result.append(current_level)
# return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []

    # Create an empty queue using deque
    dq = deque()

    # Create an empty list to store the explored nodes
    level_nodes = []

    # Add the root to the queue
    dq.append(root)

    # While the queue is not empty:
    while dq:
        # snapshot of nodes at current level
        level_size = len(dq)
        current_level = []

        # Process only the nodes that belong to this level
        for _ in range(level_size):
            popped_node = dq.popleft()
            current_level.append(popped_node.val)

            # Add each of the popped node's children to the end of the queue
            if popped_node.left:
                dq.append(popped_node.left)
            if popped_node.right:
                dq.append(popped_node.right)

        level_nodes.append(current_level)

    # Return the list of visited nodes
    return level_nodes

# Example Input Tree
#      3
#     / \
#    9  20
#       / \
#      15  7

# Input: root = 3
# Expected Output: [ [3], [9, 20], [15, 7]]

bst = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(bst))