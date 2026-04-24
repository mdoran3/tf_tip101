class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def tree_min(root):
    if root is None:
        return None
    min_val = root.val
    left_min = tree_min(root.left)
    right_min = tree_min(root.right)
    if left_min is not None:
        min_val = min(min_val, left_min)
    if right_min is not None:
        min_val = min(min_val, right_min)
    return min_val

# Example Input Tree #1: 

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 1

# Example Input Tree #2: Empty Tree (None)
# Input: root = None
# Expected Output: None

# --- Tests ---
# Tree 1: given example
tree1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
assert tree_min(tree1) == 1

# Tree 2: empty tree
assert tree_min(None) is None

# Tree 3: single node
assert tree_min(TreeNode(7)) == 7

# Tree 4: min is in right subtree
tree4 = TreeNode(10, TreeNode(15), TreeNode(3))
assert tree_min(tree4) == 3

# Tree 5: all negative values
tree5 = TreeNode(-1, TreeNode(-5), TreeNode(-3))
assert tree_min(tree5) == -5

# Tree 6: left-skewed tree
tree6 = TreeNode(8, TreeNode(5, TreeNode(2, TreeNode(1))))
assert tree_min(tree6) == 1

print("All tests passed!")