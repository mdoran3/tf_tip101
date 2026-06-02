#########################################
# PROBLEM 4: CHECK BALANCED BINARY TREE #
#########################################

# Given the root of a binary tree, return True 
# if the tree is balanced and False otherwise.

# A balanced binary tree is a binary tree in 
# which the depth of the two subtrees of every 
# node never differs by more than one.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#    a. What should we return for an empty tree (None root)?
#    b. Does "balanced" apply to every node in the tree, or just the root?

### P - Plan
# 2. Write out in plain English what you want to do:
#    Recursively compute the height of each subtree. At every node, check if the
#    left and right subtree heights differ by more than 1. If any node is
#    unbalanced, propagate a sentinel value (-1) back up to short-circuit the
#    rest of the traversal. Return True if the final height is not -1.

# 3. Translate each sub-problem into pseudocode:
#    define dfs(node):
#        if node is None: return 0
#        left_height = dfs(node.left)
#        if left_height == -1: return -1          # already unbalanced
#        right_height = dfs(node.right)
#        if right_height == -1: return -1         # already unbalanced
#        if abs(left_height - right_height) > 1: return -1   # this node unbalanced
#        return 1 + max(left_height, right_height)
#
#    return dfs(root) != -1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def is_balanced(root):
    if not root:
        return True

    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        if left_height == -1:
            return -1
        right_height = dfs(node.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return dfs(root) != -1




# Input Tree #1:

#       3
#      /  \
#     9   20
#        /  \
#       15   7
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(is_balanced(root1))  # Expected: True


# Input Tree #2:

#           1
#          / \
#         2   2
#        / \
#       3   3
#      / \
#     4   4

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)
print(is_balanced(root2))  # Expected: False


# Input Tree #3: Empty Tree
root3 = None
print(is_balanced(root3))  # Expected: True