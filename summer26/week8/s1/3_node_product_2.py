###############################
# Problem 3: 3 Node Product 2 #
###############################

'''
Given the root of a binary tree that has at most 3 nodes: 
the root, its left child, and its right child, return True 
if the value of the root is equal to the product of the 
values of its two children. Return False otherwise. If 
the root has only one child, return False.

Evaluate the time complexity of your function.
'''

### U - Understand
# 1. What are all the possible shapes of the tree, given it has "at most 3 nodes"?
#    The root could have zero, one, or two children (empty root itself is also possible).
# 2. What should happen if the root is missing a child, or is missing both children?
#    If the root has only one child (left only or right only), return False. If the
#    root itself is None, return False as well.


### P - Plan
'''
1. If the root is None, return False.
2. If the root is missing either its left child or its right child (but not both), return False.
3. Multiply the left child's value by the right child's value.
4. Compare the root's value to that product.
5. Return True if they are equal, False otherwise.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN check_tree(root)
    IF root is None
        RETURN False
    IF root.left is None OR root.right is None
        RETURN False
    product = root.left.val TIMES root.right.val
    RETURN root.val EQUALS product
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def check_tree(root):
    if root == None:
        return False
    elif not root.left or not root.right:
        return False
    elif root.val != root.left * root.right:
        return False
    elif root.val == root.left * root.right:
        return True

'''
# Example Input Tree: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: False
'''
bst1 = TreeNode(10, 10)
print(check_tree(bst1))

'''
# Example Input Tree: 
#   5
#  / \
# 5   1
# Input: root = 5
# Expected Output: True
'''
bst2 = TreeNode(5,5,1)
print(check_tree(bst2))

'''
# Example Input Tree: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False
'''
bst3 = TreeNode(5,None,2)
print(check_tree(bst3))

'''
# Example Input Tree: Empty Tree (None)
# Input: root = None
# Expected Output: False
'''
bst4 = None
print(check_tree(bst4))