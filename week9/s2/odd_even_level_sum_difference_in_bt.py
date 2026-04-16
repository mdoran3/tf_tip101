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