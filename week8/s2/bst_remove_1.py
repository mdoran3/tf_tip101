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