################################
# PROBLEM 2: BINARY TREE HEIGHT
################################

# Given the root of a binary tree, write a function height() 
# that returns the height of a binary tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we use built in max function to help us?
    # Should we use recursion in this problem? Why or Why not?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if there is not root, return 0
    # return 1 plus the max value functio of two recursive calls
        # height of root.left and height of root.right

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # if root is None:
            # return 0
        # return 1 + max(height(root.left), hieght(root.right))

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


# Example Input Tree #1

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 3
bt1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

# Example Input Tree #2 

#       4 

# Input: root = 4
# Expected Output: 1
bt2 = TreeNode(4)

##################
##### TESTS ######
##################
print(height(bt1))
print(height(bt2))