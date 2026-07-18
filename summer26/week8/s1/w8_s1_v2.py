####################################
# Problem 1: Build a Binary Tree 2 #
####################################

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


###############################
# Problem 2: 3 Node Product 1 #
###############################

'''
Given the root of a binary tree that has exactly 3 nodes: 
the root, its left child, and its right child, return True 
if the value of the root is equal to the product of the 
values of its two children. Return False otherwise.

Evaluate the time complexity of your function.
'''

### U - Understand
# 1. Can the tree ever have fewer or more than 3 nodes (e.g. a missing child)?
#    No - the problem guarantees exactly 3 nodes: root, left child, right child.
# 2. What should be returned, and based on what comparison?
#    Return True if root.val equals the product of root.left.val and root.right.val,
#    otherwise return False.


### P - Plan
'''
1. Access the value stored at the root node.
2. Access the values stored at the left and right child nodes.
3. Multiply the left child's value by the right child's value.
4. Compare the root's value to that product.
5. Return True if they are equal, False otherwise.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN check_tree(root)
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
	return root.val == root.left * root.right

'''
# Example Input Tree: 
#   10
#  /  \
# 2    5
# Input: root = 10
# Expected Output: True
'''
bst1 = TreeNode(10, 2, 5)
print(check_tree(bst1))

'''
# Example Input Tree: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False
'''
bst2 = TreeNode(5, 3, 1)
print(check_tree(bst2))



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