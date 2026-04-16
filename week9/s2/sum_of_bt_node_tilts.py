############################################
# PROBLEM 5: SUM OF BINARY TREE NODE TILTS #
############################################

# Given the root of a binary tree, return the sum of every tree node’s 
# tilt. The tilt of a tree node is the absolute difference between the 
# sum of all left subtree node values and all right subtree node values. 
# If a node does not have a left child, then the sum of the left subtree 
# node values is treated as 0. The rule is similar if the node does not 
# have a right child.

# Evaluate the time complexity of your solution. Define your variables 
# and give a rationale as to why you believe your solution has the stated 
# time complexity.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Is the tilt of a leaf node always 0 since it has no children?
    # Can node values be negative, and does that affect how we compute the absolute difference?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use a recursive post-order DFS helper that returns the sum of all values in a
# subtree. At each node, recursively get the left and right subtree sums, compute
# abs(left_sum - right_sum) as that node's tilt, and add it to a running total.
# Return node.val + left_sum + right_sum so the parent can use this node's full
# subtree sum. After the DFS completes, return the accumulated total tilt.

# 3. Translate each sub-problem into pseudocode:
# total_tilt = 0
# def subtree_sum(node):
#     if node is None: return 0
#     left_sum  = subtree_sum(node.left)
#     right_sum = subtree_sum(node.right)
#     total_tilt += abs(left_sum - right_sum)
#     return node.val + left_sum + right_sum
# subtree_sum(root)
# return total_tilt

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
        
        
def find_tilt(root):
    total_tilt = 0

    def subtree_sum(node):
        nonlocal total_tilt
        if node is None:
            return 0
        left_sum = subtree_sum(node.left)
        right_sum = subtree_sum(node.right)
        total_tilt += abs(left_sum - right_sum)
        return node.val + left_sum + right_sum

    subtree_sum(root)
    return total_tilt

# Example Input Tree #1:

#      1
#     / \
#    2   3

# Input: root = 1
# Expected Output: 1
# Explanation
# Tilt of node 2: |0 - 0| = 0 (no children)
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
# Sum of every tilt : 0 + 0 + 1 = 1

tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(find_tilt(tree1))  # Expected: 1


# Example Input Tree #2:

#       4
#      / \
#     2   9
#    / \   \
#   3   5   7

# Example Input: root = 4
# Expected Output: 15
# Tilt of node 3 : |0-0| = 0 (no children)
# Tilt of node 5 : |0-0| = 0 (no children)
# Tilt of node 7 : |0-0| = 0 (no children)
# Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
# Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
# Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
# Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15

tree2 = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))
print(find_tilt(tree2))  # Expected: 15