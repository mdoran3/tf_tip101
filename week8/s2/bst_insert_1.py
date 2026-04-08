###########################
# PROBLEM 3: BST INSERT 1
###########################

# Given the root of a binary search tree, insert a new node 
# with a given key and value into the tree. Return the root 
# of the modified tree. The tree is sorted by key. If a node 
# with the given key already exists, update the the existing 
# key’s value. You do not need to maintain a balanced tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Which node are we looking for here?
    # What are we doing trying to do with this target node?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # If there is not root, create a TreeNode object with 
        # the given params and return it
    # if the root node's key equals the key that is the parameter
        # then update this node's string value
    # if the key parameter is less than the key value of the root node
        # set the left child = to the recursive call of inser(root.left, key, value)
    # else
        # set the right child = to the recursive call of inser(root.right, key, value)
    # return the root

# 3. Translate each sub-problem into pseudocode:
    # func(root, key, value)
        # if not root:
            # retur Object(key, value)
        # if root.key == key (the param key):
            # root.val = value (the param value)
        # if key less than root.key:
            # left child = func(root.left, key, value)
        # else:
            # right child = func(root.right, key, value)
        # return root

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
   
def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)
    if root.key == key:
        root.val = value
        return root
    if key < root.key:
        root.left = insert(root.left, key, value)
    else:
         root.right = insert(root.right, key, value)
    return root

# Example Input Tree #1: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \    
#  1   6    

# Input: root = 10, key = 9, value = 'Naruto' 
# Expected Output: root = 10
# Expected Output Tree:
bt1 = TreeNode(10, None, TreeNode(5, None, TreeNode(1, None), TreeNode(6, None)), TreeNode(15, None))

#       10
#      /  \
#     /    \
#    5      15
#   / \    
#  1   6
#       \
#        9    


# Example Input Tree #2: Empty Tree (None)

# Input: root = None, key = 4, value = "Sailor Moon"
# Expected Output: root = 4
# Expected Output Tree:

#       4
bt2 = None

###############
## PRINT BST ##
###############
def print_bst(root):
    if root is None:
        print("(empty tree)")
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        left_key  = node.left.key  if node.left  else None
        right_key = node.right.key if node.right else None
        print(f"key={node.key}, val={node.val}, left={left_key}, right={right_key}")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

###############
#### TESTS ####
###############
bt1 = insert(bt1, 9, "Naruto")
bt2 = insert(bt2, 4, "Sailor Moon")

print()
print("--- Tree 1 after insert ---")
print_bst(bt1)
print()
print("--- Tree 2 after insert ---")
print_bst(bt2)