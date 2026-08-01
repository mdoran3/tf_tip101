#########################################################
# Problem 2: Sum of Node Values by Level in Binary Tree #
#########################################################

'''
Given the root of a binary tree, return a list of the sums of 
node values in each level in the binary tree.

Evaluate the time complexity of your solution. Define your variables 
and give a rationale as to why you believe your solution has the 
stated time complexity.
'''

### U - Understand
'''
1. What should be returned for an empty tree (root is None)? -> An empty
   list, since there are no levels to sum.
2. Do I need to know how many levels there are in advance, or can I discover
   that as I go? -> I can discover it as I go, by processing the tree one
   level at a time and adding a new sum to the result list for each level.
'''

### P - Plan
'''
1. If the root is None, return an empty list right away.
2. Create an empty queue (deque) and add the root to it, plus an empty
   results list.
3. While the queue is not empty, process one full level at a time:
   a. Record how many nodes are currently in the queue (that's the size of
      this level).
   b. Initialize a running sum of 0 for this level.
   c. Remove that many nodes from the front of the queue, adding each
      node's value to the level sum, and enqueueing each node's children
      (left then right) for the next level.
   d. Append the level sum to the results list.
4. Once the queue is empty, every level has been processed; return the
   results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION level_sum(root):
    IF root is None:
        RETURN empty list

    dq = empty queue
    ADD root TO dq
    sums = empty list

    WHILE dq is not empty:
        level_size = LENGTH of dq
        level_total = 0
        REPEAT level_size TIMES:
            node = REMOVE FRONT of dq
            level_total = level_total + node.val
            IF node.left is not None:
                ADD node.left TO dq
            IF node.right is not None:
                ADD node.right TO dq
        ADD level_total TO sums

    RETURN sums
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


def level_sum(root):
    if not root:
        return []

    dq = deque([root])
    sums = []

    while dq:
        level_size = len(dq)
        level_total = 0
        for _ in range(level_size):
            node = dq.popleft()
            level_total += node.val
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        sums.append(level_total)

    return sums


#####################
####### TESTS #######
#####################
'''
Example Input Tree

      4
     / \
    2   6
   / \
  1   3

Example Input: root = 4
Expected Output: [4, 8, 4]
Explanation:
Level 1: 4 -> sum = 4
Level 2: 2 + 6 -> sum = 8
Level 3: 1 + 3 -> sum = 4
'''

n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, left=n1, right=n3)
n6 = TreeNode(6)
root = TreeNode(4, left=n2, right=n6)

print(level_sum(root))