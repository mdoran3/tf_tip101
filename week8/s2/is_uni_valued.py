###########################
# PROBLEM 1: IS-UNI VALUED
###########################

# A binary tree is uni-valued if every node in the tree has 
# the same value. Given the root of a binary tree, return 
# True if the given tree is uni-valued and False otherwise.

# Evaluate the time complexity of your solution.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Can we use recursion in this problem? What might we recurse?
    # Each left and right node, what should we be checking?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if the root is None then return True
    # if the left child exists but its value does not equal root's value
        # we return False
    # if the right child exists but its value does not equal root's value
        # we return False
    # return two recursive function calls
        # one funciton call with the left child and the other with right child

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # if root is None:
            # return True
        # if root.left and root.left does not equal root.val
            # return False
        # if root.right and root.right does not equal root.val
            # return False
        # return func(left child) and func(right child)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_univalued(root):
    if root is None:
        return True
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)

# Example Input Tree #1

#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: True
bt1 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))

# Example Input Tree #2

#       1
#      / \
#     /   \
#    1     2
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: False
bt2 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(2, None, TreeNode(1)))

###############
#### TESTS ####
###############
print(is_univalued(bt1))
print(is_univalued(bt2))