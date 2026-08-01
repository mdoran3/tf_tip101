################################################
# Problem 1: Evaluate Boolean Full Binary Tree #
################################################

'''
Given the following TreeNode class, create the binary tree that 
has a root with value 5. The root should have a left child with 
value 10, and a right child with value 20.
'''

### U - Understand
    # What is a binary tree?
        # Each node has at most 2 children
        # Each child is itself a binary tree
        # The structure is setup recursively
    # How many levels can a binary search tree have and what is the 
    # only level that can be left incomplete?

### P - Plan
'''
bst = Object(root_val, left_val, right_val)
'''

# 3. Translate each sub-problem into pseudocode:
'''
bst = Object(5, 10, 20)
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

bst = TreeNode(5, 10, 20)

#####################
####### TESTS #######
#####################
print(bst.val)
print(bst.left)
print(bst.right)