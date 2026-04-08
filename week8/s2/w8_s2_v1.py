###########################
# PROBLEM 1: IS-UNI VALUED
###########################

# A binary tree is uni-valued if every node in the tree has 
# the same value. Given the root of a binary tree, return 
# True if the given tree is uni-valued and False otherwise.

# Evaluate the time complexity of your solution.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Can we use recursion in this problem? What might we recurse?
    # Each left and right node, what should we be checking?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if the root is None then return True
    # if the left child exists but its value does not equal root's value
        # we return False
    # if the right child exists but its value does not equal root's value
        # we return False
    # return two recursive function calls
        # one funciton call with the left child and the other with right child

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # if root is None:
            # return True
        # if root.left and root.left does not equal root.val
            # return False
        # if root.right and root.right does not equal root.val
            # return False
        # return func(left child) and func(right child)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def is_univalued(root):
    if root is None:
        return True
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)

# Example Input Tree #1

#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: True
bt1 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1)))

# Example Input Tree #2

#       1
#      / \
#     /   \
#    1     2
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: False
bt2 = TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(2, None, TreeNode(1)))

###############
#### TESTS ####
###############
print(is_univalued(bt1))
print(is_univalued(bt2))


################################
# PROBLEM 2: BINARY TREE HEIGHT
################################

# Given the root of a binary tree, write a function height() 
# that returns the height of a binary tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we use built in max function to help us?
    # Should we use recursion in this problem? Why or Why not?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if there is not root, return 0
    # return 1 plus the max value functio of two recursive calls
        # height of root.left and height of root.right

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # if root is None:
            # return 0
        # return 1 + max(height(root.left), hieght(root.right))

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


# Example Input Tree #1

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 3
bt1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

# Example Input Tree #2 

#       4 

# Input: root = 4
# Expected Output: 1
bt2 = TreeNode(4)

##################
##### TESTS ######
##################
print(height(bt1))
print(height(bt2))


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