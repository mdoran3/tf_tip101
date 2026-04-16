###################################################
# PROBLEM 1: LEVEL ORDER TRAVERSAL OF BINARY TREE #
###################################################

# Given the following pseudocode and the root of a binary tree, 
# return a list of the level order traversal of it’s nodes’ 
# values (i.e., from left to right, level by level).

# Evaluate the time complexity of your solution. Define your 
# variables and give a rationale as to why you believe your 
# solution has the stated time complexity.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How does a deque work and what is one of its key operations that will be useful here?
    # Why is a while loop effective here?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a list variable for visited nodes and a deque DS
    # if the root is none, just return
    # add root to the deque
    # create a while loop
        # pop from teh left of the deque and save this variable
        # add the popped variable to the visited nodes
        # if popped.left exists add it to the deque
        # if popped.right exists, add it to the deque
    # return the visited nodes list

# 3. Translate each sub-problem into pseudocode:
    # If ther tree is empty, return an empty list
    # create a deque data structure
    # create a list to store the visited nodes in order
    # append the root of the tree to the deque
    # while the deque is not empty
        # popped = popleft() from the deque
        # visited.append(popped)
        # if popped.left
            # deque.append(popped.left)
        # if popped.rigth
            # deque.append(popped.right)
    # return visited
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
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    while dq:
        popped_node = dq.popleft()
        level_nodes.append(popped_node.val)

    # Add each of the popped node's children to the end of the queue
        if popped_node.left:
            dq.append(popped_node.left)
        if popped_node.right:
            dq.append(popped_node.right)

    # Return the list of visited nodes
    return level_nodes

# Example Input Tree:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: [4, 2, 6, 1, 3]
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3
bst = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(level_order(bst))