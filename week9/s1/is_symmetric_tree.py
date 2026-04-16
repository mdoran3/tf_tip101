################################
# PROBLEM 1: IS SYMMETRIC TREE #
################################

# Given the root of a binary tree, return True if the tree’s 
# left and right subtrees are mirrors of each other (i.e., tree 
# is symmetric around its center). Return False otherwise.

# Evaluate the time complexity of your function.

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