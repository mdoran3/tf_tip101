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