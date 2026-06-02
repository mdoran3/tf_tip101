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