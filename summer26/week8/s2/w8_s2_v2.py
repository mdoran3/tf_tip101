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
