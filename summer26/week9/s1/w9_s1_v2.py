################################################
# Problem 1: Evaluate Boolean Full Binary Tree #
################################################

'''
Given the following TreeNode class, create the binary tree that 
has a root with value 5. The root should have a left child with 
value 10, and a right child with value 20.
'''

### U - Understand
    # What is a binary tree?
        # Each node has at most 2 children
        # Each child is itself a binary tree
        # The structure is setup recursively
    # How many levels can a binary search tree have and what is the 
    # only level that can be left incomplete?

### P - Plan
'''
bst = Object(root_val, left_val, right_val)
'''

# 3. Translate each sub-problem into pseudocode:
'''
bst = Object(5, 10, 20)
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

bst = TreeNode(5, 10, 20)

#####################
####### TESTS #######
#####################
print(bst.val)
print(bst.left)
print(bst.right)


################################
# Problem 2: Find Lonely Nodes #
################################

'''
Given the root of a binary tree, return a list containing the values 
of all lonely nodes in the tree. Return the list in any order.

A lonely node is a node that is the only child of its parent node. 
The root of the tree is not lonely because it does not have a parent node.

Evaluate the time complexity of your function.
'''

### U - Understand
'''
1. Can the tree contain nodes with duplicate values, and does that affect how
   I identify a lonely node? -> No, I only need the node's own value; I
   compare parent/child pointers, not values, so duplicates don't matter.
2. What should the function return for an empty tree or a tree with only a
   root node? -> An empty list, since a lonely node requires a parent with
   exactly one child, which can't happen in either case.
'''

### P - Plan
'''
1. Traverse the tree (DFS), visiting every node starting from the root.
2. At each node, check its two children:
   - If it has both a left and a right child, neither child is lonely.
   - If it has only a left child, that child is lonely.
   - If it has only a right child, that child is lonely.
3. Whenever a lonely child is found, add its value to a results list.
4. Continue the traversal into whichever children exist, regardless of
   whether they were lonely, so all descendants get checked too.
5. When traversal reaches a None node, stop (base case) and return.
6. After traversal completes, return the collected results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
FUNCTION find_lonely_nodes(root):
    lonely_nodes = empty list

    FUNCTION dfs(node):
        IF node is None:
            RETURN
        IF node.left is not None AND node.right is not None:
            dfs(node.left)
            dfs(node.right)
        ELSE IF node.left is not None:
            ADD node.left.val TO lonely_nodes
            dfs(node.left)
        ELSE IF node.right is not None:
            ADD node.right.val TO lonely_nodes
            dfs(node.right)
        # else: node is a leaf, nothing to do

    dfs(root)
    RETURN lonely_nodes
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_lonely_nodes(root):
    lonely_nodes = []

    def dfs(node):
        if not node:
            return
        if node.left and node.right:
            dfs(node.left)
            dfs(node.right)
        elif node.left:
            lonely_nodes.append(node.left.val)
            dfs(node.left)
        elif node.right:
            lonely_nodes.append(node.right.val)
            dfs(node.right)

    dfs(root)
    return lonely_nodes


#####################
####### TESTS #######
#####################
'''
Example Input Tree #1:

    1
   / \
  2   3
   \
    4

Input: root = 1
Expected Output: [4]
Explanation: Node 4 is the only lonely node. 
Node 1 is the root and is not lonely
Node 2 and 3 have the same parent and are not lonely


Example Input Tree #2:

     7
    / \
   1   4
  /   / \  
 6   5   3
          \
           2

Input: root = 7
Expected Output: [6,2]  
[2,6] is also an acceptable answer

Example Input Tree #3:

           11
          /  \
         99  88
        /      \  
       77       66
      /          \
     55           44
    /              \
   33               22       

Input: root = 11
Expected Output: [77, 55, 33, 66, 44, 22]
List elements may be returned in any order
Explanation: Nodes 99 and 88 share the same parent. Node 11 is the root.
All other nodes are lonely.
'''

# Tree #1
n4 = TreeNode(4)
n2 = TreeNode(2, right=n4)
n3 = TreeNode(3)
tree1 = TreeNode(1, left=n2, right=n3)

# Tree #2
n6 = TreeNode(6)
n1 = TreeNode(1, left=n6)
n5 = TreeNode(5)
n2b = TreeNode(2)
n3b = TreeNode(3, right=n2b)
n4b = TreeNode(4, left=n5, right=n3b)
tree2 = TreeNode(7, left=n1, right=n4b)

# Tree #3
n33 = TreeNode(33)
n55 = TreeNode(55, left=n33)
n77 = TreeNode(77, left=n55)
n99 = TreeNode(99, left=n77)
n22 = TreeNode(22)
n44 = TreeNode(44, right=n22)
n66 = TreeNode(66, right=n44)
n88 = TreeNode(88, right=n66)
tree3 = TreeNode(11, left=n99, right=n88)

print(find_lonely_nodes(tree1))
print(find_lonely_nodes(tree2))
print(find_lonely_nodes(tree3))




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