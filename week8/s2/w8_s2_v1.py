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


###########################
# PROBLEM 4: BST REMOVE 1
###########################

# Use the provided pseudocode to solve the problem below. 
# Given a key and the root of a binary search tree, remove 
# the node with the given key. Return the root of the 
# modified tree.

# The tree is sorted by key. If multiple nodes with the given 
# key exist, remove the first node you find. If you need 
# to remove a node with two children, use the in-order 
# successor of that node, which is the smallest value in 
# its right subtree. You do not need to maintain a 
# balanced tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How do we search in a Binary Search Tree?
    # Once we find the right node to remove, will it matter if that node 
    #   (1) is a leaf node, (2) has one child, (3) or has two children?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if the key is less than the key of the root, recursively call remove_bst with root.left
    # if the key is greater than the key of the root, recursively call remove_bst with root.right
    # if neither of these cases are true, we have found the target node
    # if this located node has no children, return None (essentially deleting that node)
    # if the located node has one child
        # if node has left right -> return root.right
        # if node has right child -> return root.left
    # if located node has 2 children
        # successor = root.right (start at the right child of the located node)
        # while loop though while root.left is not None and set successor = root.left every time
        # once root.left is None, we have located the next node in the chronological tree structure
        # set root.val and root.val = to successor.val and successor.key
        # now remove the successor from the right subtree by calling remove_bst(root.right, successor.key)

# 3. Translate each sub-problem into pseudocode:
    # if root = None -> return None
    # if key < root.key
        # root.left = removal_func(root.left, key)
    # if key > root.key
        # root.right = removal_func(root.right, key)
    # else -> we have found the node
        # if root.left and root.rigth == None:
            # return None (target node has no children)
        # if root.left is None (target node has one child)
            # return root.right
        # if root.right is None
            # return root.leftb (target node has one child)
        # successor = root.right
        # while successor is not None (iterate to the left to find the next ordered value)
            # successor = successor.left
        # root.key = successor.key (update root to successor value)
        # root.val = successor.val

        # root.right = removal_func(root.right, successor.key) : (this prunes the successor from the right subtree)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def remove_bst(root, key):
    if root is None:
        return None

    # Locate the node to be removed
    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        # Found the node to remove

        # Leaf node: no children
        if root.left is None and root.right is None:
            return None

        # One child: replace node with its child
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Two children: find in-order successor (smallest in right subtree)
        successor = root.right
        while successor.left is not None:
            successor = successor.left

        # Copy successor's key/value into current node
        root.key = successor.key
        root.val = successor.val

        # Remove the successor from the right subtree
        root.right = remove_bst(root.right, successor.key)

    return root

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

# Example Input Tree #1: (tree depicted using keys) 

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
bt1 = TreeNode(10, None,
        TreeNode(5, None, TreeNode(1, None), TreeNode(8, None)),
        TreeNode(15, None, TreeNode(13, None), TreeNode(16, None)))
# Input: root = 10, key = 10
# Expected Output: 13
# Expected Output Tree:

#       13
#      /  \
#     /    \
#    5      15
#   / \       \
#  1   8      16


# Example Input Tree #2: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9
bt2 = TreeNode(10, None,
        TreeNode(5, None, TreeNode(1, None), TreeNode(8, None, None, TreeNode(9, None))),
        TreeNode(15, None, TreeNode(13, None), TreeNode(16, None)))
# Input: root = 10, key = 8
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   9  13  16


# Example Input Tree #3: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8   13  16
#       \
#        9
bt3 = TreeNode(10, None,
        TreeNode(5, None, TreeNode(1, None), TreeNode(8, None, None, TreeNode(9, None))),
        TreeNode(15, None, TreeNode(13, None), TreeNode(16, None)))
# Input: root = 10, key = 9
# Expected Output: 10 (Should return a node object)
# Expected Output Tree

#       10
#      /  \
#     /    \
#    5      15
#   / \     / \
#  1   8  13  16


#################
##### TEST ######
#################
print("################")
print("FIRST BST")
print("################")
print_bst(remove_bst(bt1, 10))
print()
print()
print("################")
print("SECOND BST")
print("################")
print_bst(remove_bst(bt2, 8))
print()
print()
print("################")
print("THIRD BST")
print("################")
print_bst(remove_bst(bt3, 9))
print()
print()


####################################
# PROBLEM 5: BST IN-ORDER SUCCESSOR
####################################

# In the remove_bst() problem, we summarized the in-order successor 
# of a given node as the smallest node in the given node’s right subtree. 
# This is true if the given node has a right subtree.

# More generally, the in-order successor is the node with the 
# smallest key greater than the key of the given node. Given 
# the root of a binary search tree, and a TreeNode current, 
# write a function that returns the in-order successor of the 
# current node. Assume the tree is balanced.

# Evaluate the time complexity of your solution.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # When iterating through a BST, is it a good idea to create a new variable based on root?
    # A while loop would work best here. How do we decide whether to search the left side or right side of the BST?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a placeholder variable called successor
    # create a node to be iterated with as a copy of root
    # create a while loop for while the node still exists
    # if current's key is less than node's key, search the left hand side of the BST
        # set successor equal to node since node is greater than the current and so it could be the successor
    # if current's key is greater than node's key, search the right hand side of the BST
    # return the successor

# 3. Translate each sub-problem into pseudocode:
    # succ = None
    # node = root
    # while node:
        # if current.key < node.key:
            # successor = node
            # node = node.left
        # else
            # node = node.right
    # return successor

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode():
      def __init__(self, key, value=None, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
            
def inorder_successor(root, current):
    successor = None
    node = root

    while node:
        if current.key < node.key:
            successor = node   
            node = node.left   
        else:
            node = node.right 

    return successor
              

# Build Example Tree #1/#2:
#           10
#          /  \
#         5    15
#        / \
#       1   8
#          / \
#         6   9

n1  = TreeNode(1)
n6  = TreeNode(6)
n9  = TreeNode(9)
n8  = TreeNode(8, left=n6, right=n9)
n5  = TreeNode(5, left=n1, right=n8)
n15 = TreeNode(15)
n10 = TreeNode(10, left=n5, right=n15)  # root

# Example 1: current = node with key 5 → successor is node with key 6
succ = inorder_successor(n10, n5)
print(succ.key)
# Expected: succ is a TreeNode; succ.key == 6

# Example 2: current = node with key 6 → successor is node with key 8
succ = inorder_successor(n10, n6)
# Expected: succ is a TreeNode; succ.key == 8
print(succ.key)