#############################
# Problem 1: Is Even Values #
#############################

'''
Given the root of a binary tree, return True if every 
node in the tree has an even value and False otherwise.
'''

### U - Understand
'''
1. Can the tree be empty (root is None)? What should we return in that case?
2. Do negative values count as even/odd the same way as positive values (i.e. can node values be negative)?
'''

### P - Plan
'''
1. If the current node is None, treat it as satisfying the condition (base case).
2. Check if the current node's value is odd; if so, the whole tree fails, return False.
3. Recursively check the left subtree; if it returns False, return False.
4. Recursively check the right subtree; if it returns False, return False.
5. If the node's value is even and both subtrees passed, return True.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN is_even(node)
    IF node IS None THEN
        RETURN True
    END IF

    IF node.val MOD 2 != 0 THEN
        RETURN False
    END IF

    IF is_even(node.left) == False THEN
        RETURN False
    END IF

    IF is_even(node.right) == False THEN
        RETURN False
    END IF

    RETURN True
END is_even
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_even(root):
    if root.val % 2 != 0:
        return False
    if root.left:
        is_even(root.left)
    if root.right:
        is_even(root.right)
    return True


r'''
Example Usage:

Example Input Tree #1

      2
     / \
    /   \
   4     10
  / \     \
 6   8     12

Input: root = 2
Expected Output: True
'''
bst1 = TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(8)), TreeNode(10, None, TreeNode(12)))
print(is_even(bst1))

r'''
Example Input Tree #2

      2
     / \
    /   \
   4     2
  / \     \
 1   6     8

Input: root = 2
'''
bst2 = TreeNode(2, TreeNode(4, TreeNode(1), TreeNode(6)), TreeNode(2, None, TreeNode(8)))
print(is_even(bst2))