#######################################
# PROBLEM 5: SUM ROOT TO LEAF NUMBERS #
#######################################

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.

# A leaf node is a node with no children.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Q: Can the tree be empty (root is None)? If so, should we return 0?
# Q: Can node values be multi-digit, or are they always single digits 0-9?

### P - Plan
# 2. Write out in plain English what you want to do:
# Do a DFS traversal, carrying the current number formed so far (parent's number * 10 + current node's value).
# When we reach a leaf, add that number to the total sum.

# 3. Translate each sub-problem into pseudocode:
# dfs(node, current_number):
#   if node is None: return 0
#   current_number = current_number * 10 + node.val
#   if node is a leaf: return current_number
#   return dfs(node.left, current_number) + dfs(node.right, current_number)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
    def dfs(node, current_number):
        if node is None:
            return 0
        current_number = current_number * 10 + node.val
        if node.left is None and node.right is None:
            return current_number
        return dfs(node.left, current_number) + dfs(node.right, current_number)

    return dfs(root, 0)

# Example Input Tree #1:

#       1
#      / \
#     2   3

# Example Input: root = 1
# Expected Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
print(sum_numbers(tree1))

# Example Input Tree #2:

#       4
#      / \
#     9   0
#    / \
#   5   1

# Input: root = 4
# Expected Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
tree2 = TreeNode(4)
tree2.left = TreeNode(9)
tree2.right = TreeNode(0)
tree2.left.left = TreeNode(5)
tree2.left.right = TreeNode(1)
print(sum_numbers(tree2))  