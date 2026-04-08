###################################
# PROBLEM 1: BUILD A BINARY TREE 1
###################################

# Given the following TreeNode class, create the binary tree depicted in the image below.
#                                        10
#                                      /    \
#                                     4      6

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is a binary tree?
        # Each node has at most 2 children
        # Each child is itself a binary tree
        # The structure is setup recursively
    # How many levels can a binary search tree have and what is the only level that can be left incomplete?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # chose a variable name for the binary tree
    # set it equal to an instantiation statement of the object
    # add three parameters to the Object constructor 
        # (i.e. root value, left child value, and right child value)

# 3. Translate each sub-problem into pseudocode:
    # bt = Object(root_val, left_val, right_val)
    ########
    # TEST
    ########
    # print(bt.root_val)
    # print(bt.left_val)
    # print(bt.right_val)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

binary_tree = TreeNode(10, 4, 6)

#####################
####### TESTS #######
#####################
print(binary_tree.val)
print(binary_tree.left)
print(binary_tree.right)