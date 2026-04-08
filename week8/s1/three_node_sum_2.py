##########################
# PROBLEM 3: 3-NODE SUM 2
##########################

# Given the root of a binary tree that has at most 3 nodes: 
# the root, its left child, and its right child, return True 
# if the value of the root is equal to the sum of the values 
# of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Since we don't know how many leaf nodes there might be, what should we check in the algo?
    # Should we set a variable for anything? What do we need to track?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a variable to track the sum from the leaf nodes
    # check for existence if root and return False if doesn't exist
    # check if left child exist
        # add left child value to sum variable
    # check if right child exist
        # add right child value to sum variable
    # return boolean expression of root's value compared to the leaf sum variable

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # sum = 0
        # if root does not exist:
            # return False
        # if root.left 
            # sum = sum + root.left
        # if root.right
            # sum = sum + root.right
        # return root.val == sum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    child_sum = 0
    if not root:
        return False
    if root.left:
        child_sum += root.left
    if root.right:
        child_sum+= root.right
    return root.val == child_sum
    

# Example Input Tree #1: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: True
bt1 = TreeNode(10, 10)

# Example Input Tree #2: 
#   5
#  / \
# 3   2
# Input: root = 5
# Expected Output: True
bt2 = TreeNode(5, 3, 2)

# Example Input Tree #3: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False
bt3 = TreeNode(5, None, 2)

# Example Input Tree #4: 
# Empty Tree (None)
# Input: root = None
# Expected Output: False
bt4 = TreeNode(None)


#####################
####### TESTS #######
#####################
print(check_tree(bt1))
print(check_tree(bt2))
print(check_tree(bt3))
print(check_tree(bt4))