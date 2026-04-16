#################################
# PROBLEM 2: ROOT-TO-LEAF PATHS #
#################################

# Given the root of a binary tree, return a 
# list of all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Evaluate the time complexity of your function.

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