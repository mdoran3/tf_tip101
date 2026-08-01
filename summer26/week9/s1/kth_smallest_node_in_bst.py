#########################################
# Problem 3: Kth Smallest Node in a BST #
#########################################

'''
Given the root of a binary search tree and a positive integer k, 
return the value of the kth smallest node in the tree. All nodes 
in the tree are guaranteed to be unique.

Evaluate the time complexity of your function.
'''

### U - Understand
'''
1. Can I assume k is always valid (1 <= k <= number of nodes in the tree)? ->
   Yes, k is a positive integer and the problem doesn't ask us to handle an
   out-of-range k, so I don't need bounds checking.
2. Does the BST property (left < node < right) mean I can avoid visiting
   every node? -> Yes, an in-order traversal (left, node, right) visits BST
   nodes in ascending sorted order, so I can stop as soon as I've counted k
   nodes instead of visiting the whole tree.
'''

### P - Plan
'''
1. Traverse the tree using in-order traversal (left subtree, then node, then
   right subtree), which visits BST nodes in ascending order.
2. Keep a counter of how many nodes have been visited so far.
3. Each time a node is visited, increment the counter.
4. If the counter equals k, that node's value is the answer; store it and
   stop traversing (no need to visit remaining nodes).
5. If the counter hasn't reached k yet, continue traversing into the right
   subtree (left subtree is handled first automatically by the traversal
   order).
6. After traversal ends (either by finishing or stopping early), return the
   stored answer.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION kth_smallest(root, k):
    count = 0
    result = None

    FUNCTION inorder(node):
        IF node is None OR result is not None:
            RETURN
        inorder(node.left)
        IF result is not None:
            RETURN
        count = count + 1
        IF count == k:
            result = node.val
            RETURN
        inorder(node.right)

    inorder(root)
    RETURN result
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
def kth_smallest(root, k):
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inorder(node.left)
        if result is not None:
            return
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)

    inorder(root)
    return result



#####################
####### TESTS #######
#####################
'''
Example Input Tree

          15                     
         /  \                    
        /    \                  
       /      \                 
      10      20               
     /  \     / \            
    8   12   16 26         

Example Input: root = 15, k = 4
Expected Output: 15
Explanation: The 4th smallest value is 15.
'''

n8 = TreeNode(8)
n12 = TreeNode(12)
n10 = TreeNode(10, left=n8, right=n12)
n16 = TreeNode(16)
n26 = TreeNode(26)
n20 = TreeNode(20, left=n16, right=n26)
root = TreeNode(15, left=n10, right=n20)

print(kth_smallest(root, 4))