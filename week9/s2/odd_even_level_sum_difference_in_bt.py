###################################################
# PROBLEM 1: LEVEL ORDER TRAVERSAL OF BINARY TREE #
###################################################

# Given the root of a binary tree, return the difference between 
# the sum of all node values in odd levels and sum of all node 
# values in even levels.

# Evaluate the time complexity of your solution. Define your 
# variables and give a rationale as to why you believe your 
# solution has the stated time complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:

### P - Plan
# 2. Write out in plain English what you want to do: 

# 3. Translate each sub-problem into pseudocode:

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
    dq = deque([(root, 1)])
    result = 0
    while dq:
        node, level = dq.popleft()
        if level % 2 == 1:
            result += node.val
        else:
            result -= node.val
        if node.left:
            dq.append((node.left, level + 1))
        if node.right:
            dq.append((node.right, level + 1))
    return result

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
node3b = TreeNode(3)
node5 = TreeNode(5)
node4 = TreeNode(4, node1, node7)
node2 = TreeNode(2, None, node3b)
node3 = TreeNode(3, node5)
node8 = TreeNode(8, node4, node2)
root = TreeNode(6, node3, node8)
print(level_difference(root))
