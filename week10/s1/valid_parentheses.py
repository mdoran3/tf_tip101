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