###################################
# PROBLEM 4: FIND LEFT MOST NODE 1
###################################

# Given the root of a binary tree, write a function that 
# finds the value of the left most node in the tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can recursion help us here? Are BSTs setup for recursion?
    # What is our base case?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Check if the root exists and return None if it does not
    # Check else if a left child exists
    # If it does, then return with a recursive function call 
        # Use the left child node as the param in the func. call
    # Else we have found our left most node, so return its value

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # if root does not exist:
            # return None
        # else if root.left exists:
            # return func(root.left)
        # else:
            # return root.val

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    elif root.left:
        return left_most(root.left)
    else:
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
bt2 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))


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