###################################
# PROBLEM 1: BUILD A BINARY TREE 1
###################################

# Given the following TreeNode class, create the binary tree depicted in the image below.
#                                        10
#                                      /    \
#                                     4      6

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is a binary tree?
        # Each node has at most 2 children
        # Each child is itself a binary tree
        # The structure is setup recursively
    # How many levels can a binary search tree have and what is the only level that can be left incomplete?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # chose a variable name for the binary tree
    # set it equal to an instantiation statement of the object
    # add three parameters to the Object constructor 
        # (i.e. root value, left child value, and right child value)

# 3. Translate each sub-problem into pseudocode:
    # bt = Object(root_val, left_val, right_val)
    ########
    # TEST
    ########
    # print(bt.root_val)
    # print(bt.left_val)
    # print(bt.right_val)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

binary_tree = TreeNode(10, 4, 6)

#####################
####### TESTS #######
#####################
print(binary_tree.val)
print(binary_tree.left)
print(binary_tree.right)


##########################
# PROBLEM 2: 3-NODE SUM 1
##########################

# Given the root of a binary tree that has exactly 3 nodes: 
# the root, its left child, and its right child, return True 
# if the value of the root is equal to the sum of the values 
# of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What operator allows us to get the values in each node?
    # Is if possible to solve this algorithm in one line?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a var equal to the root's value
    # set a variable equal to the sum of the left child's value and the right child's value
    # return the boolean of the equality check of these two variables

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # root_value = root.val
        # sum_value = root.left + root.right
        # return root_value == sum_value

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	return root.val == (root.left + root.right)

# Example Input Tree #1: 
#   10
#  /  \
# 4    6
# Input: root = 10
# Expected Output: True
bt1 = TreeNode(10, 4, 6)

# Example Input Tree #2: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False
bt2= TreeNode(5, 3, 1)

#####################
####### TESTS #######
#####################
print(check_tree(bt1))
print(check_tree(bt2))


##########################
# PROBLEM 3: 3-NODE SUM 2
##########################

# Given the root of a binary tree that has at most 3 nodes: 
# the root, its left child, and its right child, return True 
# if the value of the root is equal to the sum of the values 
# of its two children. Return False otherwise.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Since we don't know how many leaf nodes there might be, what should we check in the algo?
    # Should we set a variable for anything? What do we need to track?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a variable to track the sum from the leaf nodes
    # check for existence if root and return False if doesn't exist
    # check if left child exist
        # add left child value to sum variable
    # check if right child exist
        # add right child value to sum variable
    # return boolean expression of root's value compared to the leaf sum variable

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # sum = 0
        # if root does not exist:
            # return False
        # if root.left 
            # sum = sum + root.left
        # if root.right
            # sum = sum + root.right
        # return root.val == sum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    child_sum = 0
    if not root:
        return False
    if root.left:
        child_sum += root.left
    if root.right:
        child_sum+= root.right
    return root.val == child_sum
    

# Example Input Tree #1: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: True
bt1 = TreeNode(10, 10)

# Example Input Tree #2: 
#   5
#  / \
# 3   2
# Input: root = 5
# Expected Output: True
bt2 = TreeNode(5, 3, 2)

# Example Input Tree #3: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False
bt3 = TreeNode(5, None, 2)

# Example Input Tree #4: 
# Empty Tree (None)
# Input: root = None
# Expected Output: False
bt4 = TreeNode(None)

#####################
####### TESTS #######
#####################
print(check_tree(bt1))
print(check_tree(bt2))
print(check_tree(bt3))
print(check_tree(bt4))


###################################
# PROBLEM 4: FIND LEFT MOST NODE 1
###################################

# Given the root of a binary tree, write a function that 
# finds the value of the left most node in the tree.

# Evaluate the time complexity of your function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can recursion help us here? Are BSTs setup for recursion?
    # What is our base case?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Check if the root exists and return None if it does not
    # Check else if a left child exists
    # If it does, then return with a recursive function call 
        # Use the left child node as the param in the func. call
    # Else we have found our left most node, so return its value

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # if root does not exist:
            # return None
        # else if root.left exists:
            # return func(root.left)
        # else:
            # return root.val

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    elif root.left:
        return left_most(root.left)
    else:
      return root.val

# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4
bt1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))


# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1
bt2 = TreeNode(1, None, TreeNode(2, TreeNode(3), None))


# Example Input Tree #3: 

# Input: root = None
# Output: None
bt3 = TreeNode(None)

#####################
####### TESTS #######
#####################
print(left_most(bt1))
print(left_most(bt2))
print(left_most(bt3))


###################################
# PROBLEM 5: FIND LEFT MOST NODE 2
###################################

# If you implemented the previous left_most() function iteratively, 
# implement it recursively. If you implemented it recursively, 
# implement it iteratively.

# Evaluate the time complexity of the function.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of loop should we use for an iterative approach?
    # How do we iterate through nodes in a BST, in other words, 
        # how do we update the node to the next node at each iterative step?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # while there is still a left child node of root,
        # update root to be equal to root's left child
    # Once the while loop exits, we should be at the correct node
    # Return this node's value

# 3. Translate each sub-problem into pseudocode:
    # func(root)
        # while root.left:
            # root = root.left
        # return root.val

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    while root.left:
        root = root.left
    return root.val

# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4
bt1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1
bt2 = TreeNode(1, None, TreeNode((2), TreeNode(3), None))

# Example Input Tree #3:

# Input: root = None
# Output: None
bt3 = TreeNode(None)

#####################
####### TESTS #######
#####################
print(left_most(bt1))
print(left_most(bt2))
print(left_most(bt3))