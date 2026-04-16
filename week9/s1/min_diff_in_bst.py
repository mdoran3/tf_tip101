##############################
# PROBLEM 3: MIN DIFF IN BST #
##############################

# Given the root of a binary search tree, return 
# the minimum difference between the values of 
# any two different nodes in the tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of traversal should we use?
    # is a helper fucntion or recursion needed?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a min variable equal to infinity
    # set a prev variable equal to None to track the value of the previous node
    # create a help fucnction for inorder that takes a node
        # call nonlocal on the min and prev variables for scoping
        # if there is no node: return
        # call inorder with node.left
        # if the prev is NOT set to None
            # set the min equal to either min or node.val-prev
        # prev = node.val
        # call inorder(node.right)
    # call inorder(root)
    # return min

# 3. Translate each sub-problem into pseudocode:
    # minimum = float('inf')
    # prev = None
    # def inorder(node):
        # nonlcal minimum, prev
        # if not node:
            # return
        # inorder(node.left)
        # if prev exists
            # minimum = min of (minimum, node.val - prev)
        # prev = node.val
        # inorder(node.right)
    # inorder(root)
    # return minimum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root):
    min_diff = float('inf')
    prev = None

    def inorder(node):
        nonlocal min_diff, prev
        if not node:
            return
        inorder(node.left)
        if prev is not None:
            min_diff = min(min_diff, node.val - prev)
        prev = node.val
        inorder(node.right)

    inorder(root)
    return min_diff

# Example Input Tree #1:

#     4
#    / \
#   2   6
#  / \  
# 1   3

# Example Input: root = 4
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)
bst1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(min_diff_in_bst(bst1))

# Example Input Tree  #2: 

#    1
#   / \
#  0  48
#     / \  
#    12 49

# Example Input: root = 1
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1)
bst2 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(min_diff_in_bst(bst2))