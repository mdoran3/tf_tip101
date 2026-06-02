################################
# PROBLEM 6: In-Order Traversal
################################

# Given the root of a binary tree, return a list representing the 
# inorder traversal of its nodes' values. In an inorder traversal 
# we traverse the left subtree, then the current node, then the 
# right subtree.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
	if root is None or root.val is None:
		return []
	return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Example Input Tree #1: 
#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: [1,3,2]
bt1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))

# Example Input Tree #2 : 

# Input: root = None
# Output: []
bt2 = TreeNode(None)

# Example Input Tree #3:
#     1  

# Input: root = 1
# Output: [1]
bt3 = TreeNode(1)

#####################
####### TESTS #######
#####################
print(inorder_traversal(bt1))
print(inorder_traversal(bt2))
print(inorder_traversal(bt3))