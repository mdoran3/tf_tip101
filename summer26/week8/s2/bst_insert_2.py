###########################
# Problem 3: BST INSERT 2 #
###########################

'''
Given the root of a binary search tree, insert a new node 
with a given value into the tree. Return the root of the 
modified tree. If a node with the given value already exists, 
place the new node in the right subtree. You do not need 
to maintain a balanced tree.

Evaluate the time complexity of your function.
'''

### U - Understand
'''
1. What should happen if the value being inserted already exists in the tree?
   -> The new node must be placed in the right subtree of the matching node,
      rather than the left (duplicates always go right).

2. Does the resulting tree need to stay balanced after the insert?
   -> No, we do not need to maintain a balanced tree; a normal BST insert
      following left/right ordering is sufficient.
'''

### P - Plan
'''
- BST property: left subtree < node < right subtree.
- Walk down from root: if value is less than the current node, go left;
  if value is greater than OR equal to the current node, go right
  (this naturally sends duplicates to the right, satisfying the spec).
- When we reach a None spot, that's where the new node gets created.
- Recursion naturally reattaches the (possibly new) subtree to its parent.
'''

# 3. Translate each sub-problem into pseudocode:
'''
insert(root, value):
    if root is None:
        return new TreeNode(value)
    if value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def insert_with_duplicates(root, value):
    if not root:
        return TreeNode(value)

    if value < root.val:
        root.left = insert_with_duplicates(root.left, value)
    else:
        root.right = insert_with_duplicates(root.right, value)

    return root

'''
Time Complexity: O(h), where h is the height of the tree, since we make one
recursive call per level as we walk down a single root-to-leaf path.
- Balanced tree: O(log n)
- Skewed (worst case) tree: O(n)
Space Complexity: O(h) for the recursion stack (same reasoning as above).
'''


'''
Example Usage:

Example Input Tree #1: 

      10
     /  \
    /    \
   8      15
  / \    
 1   6    

Input: root = 10, value = 9 
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \    
 1   6
      \
       9    
'''
bst1 = TreeNode(10,
                TreeNode(8, TreeNode(1), TreeNode(6)),
                TreeNode(15))
result1 = insert_with_duplicates(bst1, 9)
print(result1.val, result1.left.right.right.val)  # 10 9

'''
Example Input Tree #2: 

      10
     /  \
    /    \
   8      15
  / \    
 1   6    

Input: root = 10, value = 8
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \    
 1   6
      \
       8    

'''
bst2 = TreeNode(10,
                TreeNode(8, TreeNode(1), TreeNode(6)),
                TreeNode(15))
result2 = insert_with_duplicates(bst2, 8)
print(result2.val, result2.left.right.right.val)  # 10 8

'''
Example Input Tree #3: Empty Tree (None)

Input: root = None, value = 4
Expected Output: root = 4
Expected Output Tree:

      4 
'''
bst3 = None
new_root = insert_with_duplicates(bst3, 4)
print(new_root.val)
