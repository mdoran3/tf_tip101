########################
# Problem 1: Flowerbed #
########################

'''
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given a list of integers flowerbed containing 0's and 1's, where 0 
means empty and 1 means not empty, and an integer n, return True if 
n new flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule and False otherwise.
'''

### U - Understand
'''
1. What counts as a valid spot to plant a flower, and how do the two ends
   of the flowerbed (index 0 and the last index) affect that check?
2. What should the function return once we know how many flowers can
   actually be planted - a count, or a boolean comparison against n?
'''

### P - Plan
'''
1. Walk through the flowerbed one plot at a time, tracking how many
   flowers have been planted so far.
2. For each empty plot (0), decide whether it's plantable: skip the
   neighbor checks at the two boundary indices, otherwise only plant
   if both the left and right neighbors are empty.
3. After scanning the whole flowerbed, compare the planted count to n
   and return True if they match, False otherwise.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set i = 0
    set planted = 0

    WHILE i < length(flowerbed):
        IF flowerbed[i] == 0:
            IF i == 0:
                // boundary case, no left neighbor to check
            ELSE IF i == length(flowerbed) - 1:
                // boundary case, no right neighbor to check
            ELSE IF flowerbed[i-1] == 0 AND flowerbed[i+1] == 0:
                mark flowerbed[i] as planted
                increment planted

        increment i

    IF planted == n:
        RETURN True
    RETURN False
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def can_place_flowers(flowerbed, n):
	i = 0
	planted = 0
	while i < len(flowerbed):
		if flowerbed[i] == 0:
			if i == 0:
				pass
			elif i == len(flowerbed) - 1:
				pass
			elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
				flowerbed[i] == 1
				planted += 1
		i += 1
	if planted == n:
		return True
	return False
				
			

#####################
####### TESTS #######
#####################
'''
# Example Input: flowerbed = [1,0,0,0,1], n = 1
# Expected Output: True
'''
fb = [1,0,0,0,1]
n = 1
print(can_place_flowers(fb, n))


'''
# Example Input: flowerbed = [1,0,0,0,1], n = 2
# Expected Output: False
'''
fb = [1,0,0,0,1]
n = 2
print(can_place_flowers(fb, n))



##################################
# Problem 2: Reverse_Linked_List #
##################################

'''
Given the head of a singly linked list, reverse the list, 
and return the head of the reversed list.
'''

### U - Understand
'''
1. What does "reversing" the list actually mean in terms of each node's
   `next` pointer, rather than just the order values are printed in?
2. What should be returned as the new head, and what happens to the
   original head node's `next` pointer once the list is reversed?
'''

### P - Plan
'''
1. Walk through the list one node at a time, keeping track of the
   previously visited node (starting with none, since the new tail's
   next should point to nothing).
2. At each node, save its next node before overwriting it, then point
   the current node's next back at the previous node.
3. Advance both the "previous" and "current" pointers forward, and once
   the current pointer runs off the end of the list, the last node
   visited is the new head - return it.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set prev = None
    set curr = head

    WHILE curr is not None:
        set next_node = curr.next
        set curr.next = prev
        set prev = curr
        set curr = next_node

    RETURN prev
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
	prev = None
	curr = head
	while curr is not None:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	return prev
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input List: 1 -> 2 -> 3 -> 4
Input: head = 3, val = 1
Expected Return Value: 4
Expected Result List: 4 -> 3 -> 2 -> 1
'''
head = Node(1, Node(2, Node(3, Node(4))))
new_head = reverse(head)

result = []
node = new_head
while node is not None:
	result.append(node.value)
	node = node.next
print(result)



######################################
# Problem 3: Valid Word Abbreviation #
######################################

'''
A string can be abbreviated by replacing any number of non-adjacent, 
non-empty substrings with their lengths. The lengths should not have 
leading zeros.

For example, a string such as "substitution" could be abbreviated as 
(but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return True if the string 
matches the given abbreviation. Return False otherwise.

A substring is a contiguous non-empty sequence of characters within a 
string.
'''

### U - Understand
'''
1. How should the digits in abbr be interpreted - as a count of characters
   in word to skip over, and what makes a digit sequence invalid
   (leading zero, or replacing zero characters)?
2. Since word and abbr can be different lengths, how do we know the
   abbreviation is a valid match instead of just running out of one
   string before the other?
'''

### P - Plan
'''
1. Set up two pointers, i for word and j for abbr, both starting at 0.
2. Loop while both i and j are still within bounds of their strings.
3. If abbr[j] is a digit, first reject the whole thing if it's a
   leading zero.
4. Otherwise, consume the full run of consecutive digits starting at j,
   building up the number they represent.
5. Advance i forward by that number, since those are the characters in
   word being skipped over/replaced.
6. If abbr[j] is a letter instead, compare it directly to word[i]; if
   they don't match, the abbreviation is invalid.
7. When it's a letter match, advance both i and j by 1.
8. Repeat steps 2-7 until the loop ends because one pointer ran out.
9. Once the loop ends, check that i and j both landed exactly at the
   end of their strings - if only one did, the abbreviation doesn't
   fully account for the whole word (or vice versa), so it's invalid.
10. Return True only if both pointers reached the end at the same time,
    otherwise return False.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set i = 0
    set j = 0

    WHILE i < length(word) AND j < length(abbr):
        IF abbr[j] is a digit:
            IF abbr[j] == '0':
                RETURN False
            set num = 0
            WHILE j < length(abbr) AND abbr[j] is a digit:
                set num = num * 10 + value_of(abbr[j])
                increment j
            increment i by num
        ELSE:
            IF word[i] != abbr[j]:
                RETURN False
            increment i
            increment j

    RETURN (i == length(word)) AND (j == length(abbr))
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def valid_word_abbreviation(word, abbr):
	i = 0
	j = 0
	while i < len(word) and j < len(abbr):
		if abbr[j].isdigit():
			if abbr[j] == '0':
				return False
			num = 0
			while j < len(abbr) and abbr[j].isdigit():
				num = num * 10 + int(abbr[j])
				j += 1
			i += num
		else:
			if word[i] != abbr[j]:
				return False
			i += 1
			j += 1
	return i == len(word) and j == len(abbr)
				
			

#####################
####### TESTS #######
#####################
'''
Example  #1:
Input: word = "internationalization", abbr = "i12iz4n"
Expected Output: True
Explanation: The word "internationalization" can be abbreviated 
as "i12iz4n" ("i nternational iz atio n").

Example #2:
Input: word = "apple", abbr = "a2e"
Expected Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
'''
print(valid_word_abbreviation("internationalization", "i12iz4n"))
print(valid_word_abbreviation("apple", "a2e"))