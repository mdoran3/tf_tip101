################################
# PROBLEM 1: IS SYMMETRIC TREE #
################################

# Given the root of a binary tree, return True if the tree’s 
# left and right subtrees are mirrors of each other (i.e., tree 
# is symmetric around its center). Return False otherwise.

# Evaluate the time complexity of your function.
    # O(N) because each node gets visited once

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Should we use recursion in this problem?
    # Would a helper function be helpful?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # write a helper function that takes in the left and right from root
    # this helper function is inside the main function
    # out side of this helper function but inside the main fucntion at the bottom
        # write a return statement that calls the helper function with params root.left and root.right
    # in the helper function, if not left AND not right do not exist: return True (we hit the end)
    # in the helper function, if not left OR not right: return False because the balance is off
    # return 3 things in the helper function:
        # left.val equals right.val AND
        # helper(left.left, right.right) AND
        # helper(left.right, right.left)

# 3. Translate each sub-problem into pseudocode:
    # def func(root)
        # def helper(left, right)
            # if not left AND not right:
                # return True
            # if not left OR not right:
                # return False
            # return:
                # left.val == right.val
                # helper(left.left, right.right)
                # helper(left.right, right.left)

        # return helper(root.left, root.right)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val and
            is_mirror(left.left, right.right) and
            is_mirror(left.right, right.left)
        )
    return is_mirror(root.left, root.right)
   
# Example Tree #1:

#        1
#      /   \
#     /     \
#    2       2
#   / \     / \
#  3   4   4   3
# Input: root = 1
# Expected Output: True
bt1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(bt1))


# Example Tree #2:

#         1
#       /   \
#      /     \
#     2       2
#      \       \
#       3       3
# Input: root = 1
# Expected Output: False
bt2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(bt2))


#################################
# PROBLEM 2: ROOT-TO-LEAF PATHS #
#################################

# Given the root of a binary tree, return a 
# list of all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Evaluate the time complexity of your function.
    # O(N) because every node is visited once

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is depth first search?
    # Will we need a helper function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # create a list variable that will store paths
    # write a function called dfs
        # if no node just return
        # set a variable path and concatenate the value of the node (cast is to string)
        # if there are no children of root, append the path to paths and return
        # make two recursive calls: dfs(left, path + "->") and dfs(right, path + "->")
    # call dfs(root, "") - this is a helper dfs fucntion with root and an empty string
    # return paths

# 3. Translate each sub-problem into pseudocode:
    # def bst_paths(root):
        # paths = []
        # def dfs(node, path)
            # if not root
                # return
            # path += str(node.val)
            # if not node.left and not node.right
                # paths.append(path)
                # return 
            # dfs(node.left, path + "->")
            # dfs(node.right, path + "->")

        # dfs(root, "")
        # return paths

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def binary_tree_paths(root):
    paths = []

    def dfs(node, current_path):
        if not node:
            return
        current_path += str(node.val)
        if not node.left and not node.right: # this is where you have found a leaf node
            paths.append(current_path)
            return
        dfs(node.left, current_path + "->")
        dfs(node.right, current_path + "->")

    dfs(root, "")
    return paths   

# Example Input Tree #1:

#   1
#  / \
# 2   3
#  \  
#   5         

# Example Input: root = 1
# Expected Output: ["1->2->5", "1->3"]
# ["1->3", "1->2->5"] is also valid
bst1 = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(bst1))

# Example Input Tree #2:

#   1    

# Example Input: root = 1
# Expected Output: ["1"]
bst2 = TreeNode(1)
print(binary_tree_paths(bst2))


##############################
# PROBLEM 3: MIN DIFF IN BST #
##############################

# Given the root of a binary search tree, return 
# the minimum difference between the values of 
# any two different nodes in the tree.

# Evaluate the time complexity of your function.
    # O(N) becuase every node is visited

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of traversal should we use?
    # is a helper fucntion or recursion needed?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set a min variable equal to infinity
    # set a prev variable equal to None to track the value of the previous node
    # create a help fucnction for inorder that takes a node
        # call nonlocal on the min and prev variables for scoping
        # if there is no node: return
        # call inorder with node.left
        # if the prev is NOT set to None
            # set the min equal to either min or node.val-prev
        # prev = node.val
        # call inorder(node.right)
    # call inorder(root)
    # return min

# 3. Translate each sub-problem into pseudocode:
    # minimum = float('inf')
    # prev = None
    # def inorder(node):
        # nonlcal minimum, prev
        # if not node:
            # return
        # inorder(node.left)
        # if prev exists
            # minimum = min of (minimum, node.val - prev)
        # prev = node.val
        # inorder(node.right)
    # inorder(root)
    # return minimum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root):
    min_diff = float('inf')
    prev = None

    def inorder(node):
        nonlocal min_diff, prev
        if not node:
            return
        inorder(node.left)
        if prev is not None:
            min_diff = min(min_diff, node.val - prev)
        prev = node.val
        inorder(node.right)

    inorder(root)
    return min_diff

# Example Input Tree #1:

#     4
#    / \
#   2   6
#  / \  
# 1   3

# Example Input: root = 4
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)
bst1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(min_diff_in_bst(bst1))

# Example Input Tree  #2: 

#    1
#   / \
#  0  48
#     / \  
#    12 49

# Example Input: root = 1
# Expected Output: 1 
# Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1)
bst2 = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(min_diff_in_bst(bst2))


###########################################
# PROBLEM 4: INCREASING ORDER SEARCH TREE #
###########################################

# Given the root of a binary search tree, rearrange the 
# tree in in-order so that the leftmost node of the tree 
# is now the root of tree and every node has no left 
# child and only one right child.

# Return the root of the modified tree

# Evaluate the time complexity of your function.
    # O(N) every node is visited once

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What kind of traversal should be used?
    # Would a swap operation be helpful here?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # set two variables, one as temp and set it equal to curr.
    # Call the helper function with root as a param
    # return temp.right
    # in inorder(node)
        # if node does not exist: return None
        # call helper(node.left)
        # do the swap operation
        # call helper(node.rigth)

# 3. Translate each sub-problem into pseudocode:
    # temp = TreeNode(0)
    # current = temp
    # def inroder(node)
        # if not node
            # return 
        # inorder(node.left)
        # node.left = None
        # current.right = node
        # current = node
        # inorder(root.right)
    
    # inorder(root)
    # return root.right

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_bst(root):
    if not root:
        print("Empty tree")
        return

    def _print(node, prefix, is_left):
        if node is None:
            return
        _print(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        _print(node.left, prefix + ("    " if is_left else "│   "), True)

    _print(root.right, "    ", False)
    print(str(root.val))
    _print(root.left, "    ", True)

def increasing_bst(root):
    temp = TreeNode(0)
    curr = temp

    def inorder(node):
        nonlocal curr
        if not node:
            return
        inorder(node.left)
        node.left = None
        curr.right = node
        curr = node
        inorder(node.right)

    inorder(root)
    return temp.right

# Example Input Tree #1:

#     5
#    / \
#   1   7

# Example Input: root = 5
# Expected Output: root = 1
# Expected Output Tree #1:
bst1 = TreeNode(5, TreeNode(1), TreeNode(7))
print_bst(increasing_bst(bst1))

# 1 
#  \
#   5
#    \
#     7


# Example Input Tree #2:

#        5
#       / \
#      /   \
#     3     6
#    / \     \  
#   2   4     8
#  /         / \
# 1         7   9

# Input: root = 5
# Expected Output: root = 1
# Expected Output Tree #2:
bst2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
print_bst(increasing_bst(bst2))

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5 
#          \
#           6
#            \
#             7
#              \
#               8
#                \ 
#                 9


###############################
# PROBLEM 5: EQUAL TREE SPLIT #
###############################

# Given the root of a binary tree, return True if removing an 
# edge between two nodes can split the tree into two trees
# with an equal number of nodes. Return False otherwise.

# Evaluate the time complexity of the function.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # Can the tree have only one node? 
    # Are all node values unique, or can there be duplicates? 

### P - Plan
# 2. Write out in plain English what you want to do:
#    First, count the total number of nodes in the tree. If that total is odd,
#    return False immediately since an equal split is impossible. Otherwise,
#    do a post-order DFS where each call returns the size of its subtree. If
#    any subtree (other than the full tree itself) has size equal to total // 2,
#    we know cutting the edge above it produces two equal halves, so return True.

# 3. Translate each sub-problem into pseudocode:
#    count(node):
#        if node is None: return 0
#        return 1 + count(left) + count(right)
#
#    can_split(root):
#        total = count(root)
#        if total % 2 != 0: return False
#        half = total // 2
#
#        dfs(node):
#            if node is None: return 0
#            size = 1 + dfs(left) + dfs(right)
#            if size == half and node != root: mark found
#            return size
#
#        run dfs(root)
#        return found

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_split(root):
    def count(node):
        if node is None:
            return 0
        return 1 + count(node.left) + count(node.right)

    total = count(root)
    if total % 2 != 0:
        return False
    half = total // 2

    found = [False]

    def dfs(node):
        if node is None:
            return 0
        size = 1 + dfs(node.left) + dfs(node.right)
        if size == half and node is not root:
            found[0] = True
        return size

    dfs(root)
    return found[0]

# Example Input Tree #1:

#        1
#       / \
#      /   \
#     2     3
#    / \     \  
#   4   5     7

bst1 = TreeNode(1)
bst1.left = TreeNode(2)
bst1.right = TreeNode(3)
bst1.left.left = TreeNode(4)
bst1.left.right = TreeNode(5)
bst1.right.right = TreeNode(7)
print(can_split(bst1))

# Example Input: root = 1
# Expected Output: True
# Explanation: Deleting the edge between node 1 and its left child, node 2 gives the following
# two trees, each of size 3

#   Tree 1    Tree 2        
#               1
#                \
#     2           3
#    / \           \  
#   4   5           7



# Example Input Tree #2:

#        1
#       /  \
#      /    \
#     2      3
#    / \    / \  
#   4   5  6   7

bst2 = TreeNode(1)
bst2.left = TreeNode(2)
bst2.right = TreeNode(3)
bst2.left.left = TreeNode(4)
bst2.left.right = TreeNode(5)
bst2.right.left = TreeNode(6)
bst2.right.right = TreeNode(7)
print(can_split(bst2))
# Example Input: root = 1
# Expected Output: False
# Explanation: It is not possible to split the tree into two trees of equal size by deleting
# an edge