##############################
# Problem 2: Binary Tree Max #
##############################

'''
Given the root of a binary tree, write a function tree_max() 
that returns the node with the greatest value inside of a binary 
tree. If the tree is empty return None.
'''

### U - Understand
'''
1. Does the function need to return the node with the max value, or just the max value itself?
2. Can the tree contain duplicate values, and if so, does it matter which node (of equal max value) is returned?
'''

### P - Plan
'''
1. Handle the base case: if the root is None, return None.
2. Recursively find the max value/node in the left subtree.
3. Recursively find the max value/node in the right subtree.
4. Compare the root's value against the max found in the left and right subtrees.
5. Return whichever of the three (root, left max, right max) holds the greatest value.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
  FUNCTION tree_max(root):
    IF root is None:
      RETURN None

    left_max = tree_max(root.left)
    right_max = tree_max(root.right)

    max_node = root
    IF left_max is not None AND left_max.val > max_node.val:
      max_node = left_max
    IF right_max is not None AND right_max.val > max_node.val:
      max_node = right_max

    RETURN max_node
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

maximum = float("-inf") 
def tree_max(root):
    if root == None:
        return None
    global maximum
    maximum = max(maximum, root.val)
    if root.left:
        tree_max(root.left)
    if root.right:
        tree_max(root.right)
    return maximum
'''
Example Usage:

Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 5
'''
bst1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(tree_max(bst1))

'''
Example Input Tree #2: Empty Tree (None)
Input: root = None
Expected Output: None
'''
bst2 = None
print(tree_max(bst2))