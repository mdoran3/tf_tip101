##########################
# PROBLEM 2: 3-NODE SUM 1
##########################

# Given the root of a binary tree that has exactly 3 nodes: 
# the root, its left child, and its right child, return True 
# if the value of the root is equal to the sum of the values 
# of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What operator allows us to get the values in each node?
    # Is if possible to solve this algorithm in one line?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a var equal to the root's value
    # set a variable equal to the sum of the left child's value and the right child's value
    # return the boolean of the equality check of these two variables

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # root_value = root.val
        # sum_value = root.left + root.right
        # return root_value == sum_value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	return root.val == (root.left + root.right)

# Example Input Tree #1: 
#   10
#  /  \
# 4    6
# Input: root = 10
# Expected Output: True
bt1 = TreeNode(10, 4, 6)

# Example Input Tree #2: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False
bt2= TreeNode(5, 3, 1)


#####################
####### TESTS #######
#####################
print(check_tree(bt1))
print(check_tree(bt2))