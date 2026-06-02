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