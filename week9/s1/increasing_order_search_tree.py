###########################################
# PROBLEM 4: INCREASING ORDER SEARCH TREE #
###########################################

# Given the root of a binary search tree, rearrange the 
# tree in in-order so that the leftmost node of the tree 
# is now the root of tree and every node has no left 
# child and only one right child.

# Return the root of the modified tree

# Evaluate the time complexity of your function.
    # O(N) every node is visited once

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of traversal should be used?
    # Would a swap operation be helpful here?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set two variables, one as temp and set it equal to curr.
    # Call the helper function with root as a param
    # return temp.right
    # in inorder(node)
        # if node does not exist: return None
        # call helper(node.left)
        # do the swap operation
        # call helper(node.rigth)

# 3. Translate each sub-problem into pseudocode:
    # temp = TreeNode(0)
    # current = temp
    # def inroder(node)
        # if not node
            # return 
        # inorder(node.left)
        # node.left = None
        # current.right = node
        # current = node
        # inorder(root.right)
    
    # inorder(root)
    # return root.right

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_bst(root):
    if not root:
        print("Empty tree")
        return

    def _print(node, prefix, is_left):
        if node is None:
            return
        _print(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        _print(node.left, prefix + ("    " if is_left else "│   "), True)

    _print(root.right, "    ", False)
    print(str(root.val))
    _print(root.left, "    ", True)

def increasing_bst(root):
    temp = TreeNode(0)
    curr = temp

    def inorder(node):
        nonlocal curr
        if not node:
            return
        inorder(node.left)
        node.left = None
        curr.right = node
        curr = node
        inorder(node.right)

    inorder(root)
    return temp.right

# Example Input Tree #1:

#     5
#    / \
#   1   7

# Example Input: root = 5
# Expected Output: root = 1
# Expected Output Tree #1:
bst1 = TreeNode(5, TreeNode(1), TreeNode(7))
print_bst(increasing_bst(bst1))

# 1 
#  \
#   5
#    \
#     7


# Example Input Tree #2:

#        5
#       / \
#      /   \
#     3     6
#    / \     \  
#   2   4     8
#  /         / \
# 1         7   9

# Input: root = 5
# Expected Output: root = 1
# Expected Output Tree #2:
bst2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
print_bst(increasing_bst(bst2))

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5 
#          \
#           6
#            \
#             7
#              \
#               8
#                \ 
#                 9