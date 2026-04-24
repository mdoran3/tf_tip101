################################
# PROBLEM 1: VALID PARENTHESES #
################################

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# return True if the input string is valid and False otherwise.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
	# What data structure can we use to add parenthese and remove them that 
		# would work well in this problem?
	# How many times might we need to iterate through the input string?

### P - Plan
# 2. Write out in plain English what you want to do: 
	# create a dict with parentheses pairs
	# create a list with open brackets
	# create a list with closed brackets
	# create an empty stack
	# use a for loop to iterate through the passed in parameter
	# if the element is in the open brackets, add it to the empty stack
	# if it is in the close brackets string and that value in paris matches the key
		# pop it off the stack
	# if the stack is empty return true, else return false

# 3. Translate each sub-problem into pseudocode:
	# pairs = {} # key = close bracket, value = open brack for (), [], and {}
	# open = "([{"
	# close = ")]}"
	# parens = []
	# for item in string
		# if item in open
			# append it to parens
		# if item in close AND last item of parens == the key of pairs[item]
			# pop and item off the parens stack
	# if parens is empty    
		# return True
	# return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_valid(s):
	pairs = {")" : "(", "]" : "[", "}" : "{"}
	open = "([{"
	close = ")]}"
	parens = []
	for char in s:
		if char in open:
			parens.append(char)
		# print(f"CHAR: {char}") # DEBUG
		# print(f"LAST ITEM IN PARENS: {parens[len(parens)-1]}") # DEBUG
		if char in close and parens[len(parens)-1] == pairs[char]:
			parens.pop()
	if not parens:
		return True
	return False

# Example #1:
# Input: s = "()"
# Expected Output: True
s1 = "()"
print(is_valid(s1))

# Example #2:
# s = "()[]{}"
# Expected Output: True
s2 = "()[]{}"
print(is_valid(s2))

# Example #3: 
# s = "(())"
# Expected Output: True
s3 = "(())"
print(is_valid(s3))

# Example #4:
# s = "(]"
# Expected Output: False
s4 = "(]"
print(is_valid(s4))

# Example #5:
# s = "([)]"
# Expected Output: False
s5= "([)]"
print(is_valid(s5))

###############################################
# PROBLEM 2: BEST TIME TO BUTY AND SELL STOCK #
###############################################

# You are given a list of integers prices where prices[i] 
# is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single 
# day to buy one stock and choosing a different day in the 
# future to sell that stock.

# Return the maximum profit you can achieve from this 
# transaction. If you cannot achieve any profit, return 0.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How should we iterate through prices? For loop? While loop? 
    # How mamy pointers should we use?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Initialize some variables like:
        # an initial buy price at the 0th index of prices
        # an initial sell price at the last index of prices
        # front pointer to 0
        # back pointer to the length of prices - 1
        # initial profit to sell - buy ( which is the highest prices minus the largest price)
    # Use a while loop while the two pointers do not cross
    # Check profit for if you increment front pointer and check profit for if the back pointer decremented
    # which ever one is greater, update the profit by comparing that result to the current profit
    # increment the front or decrement the back accordingly
    # return profit if above 0, else just return 0

# 3. Translate each sub-problem into pseudocode:
    # buy = prices[0]
    # sell = prices[last index]
    # front = 0
    # back = last index
    # profit = sell - buy
    # while front < back
        # forward_profit = prices[back] - prices[front + 1]
        # backward_profit = prices[back - 1] - prices[front]
        # if forward_profit > backward_profit
            # profit = max(profit, forward_profit)
            # increment front
        # else
            # profit = max(profit, backward_profit)
            # decrement back
    # if profit > 0
        # return profit
    # return 0


### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def max_profit(prices):
    buy = prices[0]
    sell = prices[len(prices)-1]
    front = 0
    back = len(prices) - 1
    profit = sell - buy
    while front < back:
        forward = prices[back] - prices[front+1]
        backward = prices[back-1] - prices[front]
        if forward > backward:
            profit = max(profit, forward)
            front += 1
        else:
            profit = max(profit, backward)
            back -= 1
    if profit > 0:
        return profit
    return 0
    
# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
prices = [7,1,5,3,6,4]
print(max_profit(prices))

# Example #2:
# Input: prices = [7,6,4,3,1]
# Expected Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
prices1 = [7,6,4,3,1]
print(max_profit(prices1))


############################
# PROBLEM 3: SHUFFLE MERGE #
############################

# Given the heads of two singly linked lists of integers, 
# merge their nodes to make one list, taking nodes alternately 
# between the two lists. If either list runs out of elements 
# before the other, all nodes from the list with remaining 
# nodes should be appended onto the end of the merged list. 
# Return the head of the merged list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we iterate through and alternate between lists?
    # Do we need to create a new list? What is the space complexity? 

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a new linked list by initializing a node and naming it.
    # make a copy of it to iterate with
    # use a while loop to iterate while either of the lists are still valid
    # take the head of one list and create a new ListNode and set your new LL .next to this node.
        # decrement up in that LL and the new LL
    # Repeat this for the next list to be joined
    # return the non copied version of the list created and return its head as its .next

# 3. Translate each sub-problem into pseudocode:
    # temp = ListNode(0)
    # current = temp
    # while head_a or head_b:
    #     if head_a:
    #         current.next = ListNode(head_a.val)
    #         current = current.next
    #         head_a = head_a.next
    #     if head_b:
    #         current.next = ListNode(head_b.val)
    #         current = current.next
    #         head_b = head_b.next
    # return temp.next

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class ListNode:
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

def print_linked_list(head):
	values = []
	while head:
		values.append(str(head.val))
		head = head.next
	print(" -> ".join(values))

def shuffle_merge(head_a, head_b):
	temp = ListNode(0)
	shuffled = temp

	while head_a or head_b:
		if head_a:
			node_a = ListNode(head_a.val)
			shuffled.next = node_a
			shuffled = shuffled.next
			head_a = head_a.next
		if head_b:
			node_b = ListNode(head_b.val)
			shuffled.next = node_b
			shuffled = shuffled.next
			head_b = head_b.next
	return temp.next

# Test 1: List 1: 1 -> 2 -> 3, List 2: 4 -> 5 -> 6
# Expected: 1 -> 4 -> 2 -> 5 -> 3 -> 6
a1 = ListNode(1, ListNode(2, ListNode(3)))
b1 = ListNode(4, ListNode(5, ListNode(6)))
print_linked_list(shuffle_merge(a1, b1))

# Test 2: List 1: 1 -> 2 -> 3, List 2: 4
# Expected: 1 -> 4 -> 2 -> 3
a2 = ListNode(1, ListNode(2, ListNode(3)))
b2 = ListNode(4)
print_linked_list(shuffle_merge(a2, b2))


#############################
# PROBLEM 4: GROUP ANAGRAMS #
#############################

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all 
# the original letters exactly once.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
	# Can the input contain empty strings, and should they be grouped together?
	# Are the strings case-sensitive, meaning "Eat" and "eat" would NOT be anagrams?

### P - Plan
# 2. Write out in plain English what you want to do:
	# Create a hashmap where the key is a sorted version of each word
	# and the value is a list of all words that sort to that same key
	# Iterate through strs, sort each word to get its key,
	# and append the word to the corresponding list in the hashmap
	# Return all the values in the hashmap as a list of lists

# 3. Translate each sub-problem into pseudocode:
	# anagram_map = {}
	# for word in strs
		# key = "".join(sorted(word))
		# if key not in anagram_map
			# anagram_map[key] = []
		# append word to anagram_map[key]
	# return list of anagram_map.values()

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def group_anagrams(strs):
	anagrams = []
	for word in strs:
		sorted_word = "".join(sorted(word))
		if not anagrams:
			anagrams.append([word])
		else:
			toggle = 0
			for ana_words in anagrams:
				anagram_sorted = "".join(sorted(ana_words[0]))
				if anagram_sorted == sorted_word:
					ana_words.append(word)
					toggle = 1
					break
			# Check toggle if word has been appended
			if toggle == 0:
				anagrams.append([word])
			# Reset toggle
			if toggle == 1:
				toggle = 0
	return anagrams

# Example #1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
s = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(s))

# Example #2:
# Input: strs = [""]
# Expected Output: [[""]]
s1 = [""]
print(group_anagrams(s1))

# Example #3:
# Input: strs = ["a"]
# Expected Output: [["a"]]
s2 = ["a"]
print(group_anagrams(s2))


#######################################
# PROBLEM 5: SUM ROOT TO LEAF NUMBERS #
#######################################

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers.

# A leaf node is a node with no children.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
# Q: Can the tree be empty (root is None)? If so, should we return 0?
# Q: Can node values be multi-digit, or are they always single digits 0-9?

### P - Plan
# 2. Write out in plain English what you want to do:
# Do a DFS traversal, carrying the current number formed so far (parent's number * 10 + current node's value).
# When we reach a leaf, add that number to the total sum.

# 3. Translate each sub-problem into pseudocode:
# dfs(node, current_number):
#   if node is None: return 0
#   current_number = current_number * 10 + node.val
#   if node is a leaf: return current_number
#   return dfs(node.left, current_number) + dfs(node.right, current_number)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
    def dfs(node, current_number):
        if node is None:
            return 0
        current_number = current_number * 10 + node.val
        if node.left is None and node.right is None:
            return current_number
        return dfs(node.left, current_number) + dfs(node.right, current_number)

    return dfs(root, 0)

# Example Input Tree #1:

#       1
#      / \
#     2   3

# Example Input: root = 1
# Expected Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
print(sum_numbers(tree1))

# Example Input Tree #2:

#       4
#      / \
#     9   0
#    / \
#   5   1

# Input: root = 4
# Expected Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
tree2 = TreeNode(4)
tree2.left = TreeNode(9)
tree2.right = TreeNode(0)
tree2.left.left = TreeNode(5)
tree2.left.right = TreeNode(1)
print(sum_numbers(tree2))  