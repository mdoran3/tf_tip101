###########################
# PROBLEM 4: BST REMOVE 1
###########################

# Use the provided pseudocode to solve the problem below. 
# Given a key and the root of a binary search tree, remove 
# the node with the given key. Return the root of the 
# modified tree.

# The tree is sorted by key. If multiple nodes with the given 
# key exist, remove the first node you find. If you need 
# to remove a node with two children, use the in-order 
# successor of that node, which is the smallest value in 
# its right subtree. You do not need to maintain a 
# balanced tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:

### P - Plan
# 2. Write out in plain English what you want to do: 

# 3. Translate each sub-problem into pseudocode:

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def remove_bst(root, key):
    if root is None:
        return None

    # Locate the node to be removed
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        # Found the node to remove

        # Leaf node: no children
        if root.left is None and root.right is None:
            return None

        # One child: replace node with its child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Two children: find in-order successor (smallest in right subtree)
        successor = root.right
        while successor.left is not None:
            successor = successor.left

        # Copy successor's key/value into current node
        root.key = successor.key
        root.val = successor.val

        # Remove the successor from the right subtree
        root.right = remove_bst(root.right, successor.key)

    return root



# Example Input Tree #1: (tree depicted using keys) 

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16


# Input: root = 10, key = 10
# Expected Output: 13
# Expected Output Tree:

#       13
#      /  \
#     /    \
#    5      15
#   / \       \
#  1   8      16


# Example Input Tree #2: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 8
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   9  13  16


# Example Input Tree #3: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9 

# Input: root = 10, key = 9
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8  13  16