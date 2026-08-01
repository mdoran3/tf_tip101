########################################################
# Problem 3: Maximum Nodes at Any Level in Binary Tree #
########################################################

'''
Given the root of a binary tree, return the maximum number of 
nodes in any level of the binary tree.

Evaluate the time complexity of your solution. Define your 
variables and give a rationale as to why you believe your solution 
has the stated time complexity.
'''

### U - Understand
'''
1. What should be returned for an empty tree (root is None)? -> 0, since
   there are no levels and therefore no nodes at any level.
2. Do I need the sums or values of the nodes, or just how many nodes are at
   each level? -> Just the count of nodes at each level; I only need to
   track the size of each level as I traverse and keep the largest one.
'''

### P - Plan
'''
1. If the root is None, return 0 right away.
2. Create an empty queue (deque) and add the root to it, plus a variable to
   track the maximum level size seen so far (start at 0).
3. While the queue is not empty, process one full level at a time:
   a. Record how many nodes are currently in the queue (that's the size of
      this level).
   b. Update the maximum if this level's size is larger than what's been
      seen so far.
   c. Remove that many nodes from the front of the queue, enqueueing each
      node's children (left then right) for the next level.
4. Once the queue is empty, every level has been processed; return the
   maximum level size found.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION level_max(root):
    IF root is None:
        RETURN 0

    dq = empty queue
    ADD root TO dq
    max_count = 0

    WHILE dq is not empty:
        level_size = LENGTH of dq
        max_count = MAX(max_count, level_size)
        REPEAT level_size TIMES:
            node = REMOVE FRONT of dq
            IF node.left is not None:
                ADD node.left TO dq
            IF node.right is not None:
                ADD node.right TO dq

    RETURN max_count
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_max(root):
    if not root:
        return 0

    dq = deque([root])
    max_count = 0

    while dq:
        level_size = len(dq)
        max_count = max(max_count, level_size)
        for _ in range(level_size):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

    return max_count

#####################
####### TESTS #######
#####################
'''
Example Usage:

Example Input Tree #1:

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: 2
Explanation: Levels 2 & 3 have 2 nodes each. 

Example Input Tree #2:

       1
      / \
     /   \
    2     3
   / \   / \ 
  4   5 6   7

Example Input: root = 1
Expected Output: 4
Explanation: Level 3 has 4 nodes, the most of any level
'''

# Tree #1
n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, left=n1, right=n3)
n6 = TreeNode(6)
tree1 = TreeNode(4, left=n2, right=n6)

# Tree #2
n4 = TreeNode(4)
n5 = TreeNode(5)
n2b = TreeNode(2, left=n4, right=n5)
n6b = TreeNode(6)
n7 = TreeNode(7)
n3b = TreeNode(3, left=n6b, right=n7)
tree2 = TreeNode(1, left=n2b, right=n3b)

print(level_max(tree1))
print(level_max(tree2))