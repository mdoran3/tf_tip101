###################################
# PROBLEM 5: FIND LEFT MOST NODE 2
###################################

# If you implemented the previous left_most() function iteratively, 
# implement it recursively. If you implemented it recursively, 
# implement it iteratively.

# Evaluate the time complexity of the function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of loop should we use for an iterative approach?
    # How do we iterate through nodes in a BST, in other words, 
        # how do we update the node to the next node at each iterative step?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # while there is still a left child node of root,
        # update root to be equal to root's left child
    # Once the while loop exits, we should be at the correct node
    # Return this node's value

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # while root.left:
            # root = root.left
        # return root.val

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    while root.left:
        root = root.left
    return root.val

# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4
bt1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1
bt2 = TreeNode(1, None, TreeNode((2), TreeNode(3), None))

# Example Input Tree #3:

# Input: root = None
# Output: None
bt3 = TreeNode(None)

#####################
####### TESTS #######
#####################
print(left_most(bt1))
print(left_most(bt2))
print(left_most(bt3))