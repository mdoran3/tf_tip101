#####################################################################
# PROBLEM 4: LEVEL ORDER TRAVERSAL OF BINARY TREE WITH NESTED LISTS #
#####################################################################

# Given the root of a binary tree, write a function level_order() that returns 
# the level order traversal of its nodes’ values (i.e., from left to right, 
# level by level). level_order() should return a list of lists, where each 
# inner list contains the node values of a single level in the tree.

# Evaluate the time complexity of your solution. Define your variables and 
# give a rationale as to why you believe your solution has the stated time 
# complexity.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # How can we sure we are only dealing with one level at a time i the while loop?
    # Should we return an empty list if the root is None, or raise an error?

### P - Plan
# 2. Write out in plain English what you want to do:
# Use BFS with a queue. Start by adding the root to the queue.
# On each iteration, snapshot the current queue size so we know how many nodes
# belong to the current level. Process exactly that many nodes, collecting their
# values into a sub-list, and enqueue their children. Append the sub-list to the
# result. Repeat until the queue is empty, then return the result.

# 3. Translate each sub-problem into pseudocode:
# if root is None: return []
# queue = deque([root])
# result = []
# while queue is not empty:
#     level_size = len(queue)
#     current_level = []
#     for i in range(level_size):
#         node = queue.popleft()
#         current_level.append(node.val)
#         if node.left:  queue.append(node.left)
#         if node.right: queue.append(node.right)
#     result.append(current_level)
# return result

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []

    # Create an empty queue using deque
    dq = deque()

    # Create an empty list to store the explored nodes
    level_nodes = []

    # Add the root to the queue
    dq.append(root)

    # While the queue is not empty:
    while dq:
        # snapshot of nodes at current level
        level_size = len(dq)
        current_level = []

        # Process only the nodes that belong to this level
        for _ in range(level_size):
            popped_node = dq.popleft()
            current_level.append(popped_node.val)

            # Add each of the popped node's children to the end of the queue
            if popped_node.left:
                dq.append(popped_node.left)
            if popped_node.right:
                dq.append(popped_node.right)

        level_nodes.append(current_level)

    # Return the list of visited nodes
    return level_nodes

# Example Input Tree
#      3
#     / \
#    9  20
#       / \
#      15  7

# Input: root = 3
# Expected Output: [ [3], [9, 20], [15, 7]]

bst = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(level_order(bst))