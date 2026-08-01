########################
# Problem 1: Flip Game #
########################

'''
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. 
You and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move, and therefore 
the other person will be the winner.

Return all possible states of the string currentState after one valid 
move. You may return the answer in any order. If there is no valid move, 
return an empty list [].
'''

### U - Understand
'''
1. What counts as a valid move, and where in the string can it happen -
   does it only apply to the exact pair "++", not any longer run
   of pluses treated as a single unit?
2. Since a move can be made starting at any position where "++" occurs,
   how many total valid moves (and therefore output strings) might
   there be for a given input, and does order matter?
'''

### P - Plan
'''
1. Create an empty list to collect all the resulting states after one
   valid move.
2. Scan through current_state one index at a time, from the start up to
   (but not including) the second-to-last character, since a move needs
   a pair of characters.
3. At each index i, check whether current_state[i] and current_state[i+1]
   are both '+'.
4. If they are, that's a valid move: build a new string by taking the
   part of current_state before index i, inserting "--" in place of the
   "++", and appending the part of current_state after index i+1.
5. Add that new string to the results list.
6. If the pair at index i is not "++", skip it and move to the next index.
7. After scanning the whole string, return the results list - if no
   valid moves were found, it will simply be empty.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set moves = empty list

    FOR i FROM 0 TO length(current_state) - 2:
        IF current_state[i] == '+' AND current_state[i+1] == '+':
            set new_state = current_state[0..i] + "--" + current_state[i+2..end]
            append new_state to moves

    RETURN moves
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def generate_possible_next_moves(current_state):
	moves = []
	for i in range(len(current_state) - 1):
		if current_state[i] == '+' and current_state[i+1] == '+':
			moves.append(current_state[:i] + '--' + current_state[i+2:])
	return moves
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input: current_state = "++++"
Output: ["--++","+--+","++--"]
'''
print(generate_possible_next_moves("++++"))

'''
Example #2:
Input: current_state = "+"
Output: []
'''
print(generate_possible_next_moves("+"))



########################################
# Problem 2: Intersection of Two Words #
########################################

'''
Given two lists of integers nums1 and nums2, return a list of 
their intersection. Each element in the result list must be 
unique and you may return the result in any order.
'''

### U - Understand
'''
1. What does "intersection" mean here - a value that appears in both
   lists at least once - and how should duplicate values within a
   single list be handled in the output?
2. Does it matter which list we iterate over first, and how many times
   a value appears in each list (versus just whether it appears at all)?
'''

### P - Plan
'''
1. Figure out which of the two input lists is shorter and which is
   longer, since it's cheaper to loop over the shorter one.
2. Create an empty list to collect the intersection results.
3. Loop through each value in the shorter list one at a time.
4. For each value, check whether it also exists somewhere in the
   longer list.
5. If it exists in the longer list AND hasn't already been added to
   the results (to avoid duplicates), append it to the results list.
6. If it doesn't exist in the longer list, or it's already in the
   results, skip it and move to the next value.
7. After scanning the whole shorter list, return the results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set short = the shorter of nums1 and nums2
    set long = the longer of nums1 and nums2
    set intersections = empty list
    set i = 0

    WHILE i < length(short):
        IF short[i] is in long AND short[i] is not in intersections:
            append short[i] to intersections
        increment i

    RETURN intersections
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def intersection(nums1, nums2):
	short = []
	long = []
	intersections = []
	i = 0
	if len(nums1) < len(nums2):
		short = nums1
		long = nums2
	if len(nums2) <= len(nums1):
		short = nums2
		long = nums1
	while i < len(short):
		if short[i] in long and short[i] not in intersections:
			intersections.append(short[i])
		i += 1
	return intersections
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
'''
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

'''
Example #2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Expected Output: [9, 4]
[4, 9] is also an acceptable answer.
'''
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))



###########################################
# Problem 3: Buildings with an Ocean View #
###########################################

'''
There are n buildings in a line. You are given an list of integers 
heights of size n that represents the heights of the buildings in 
the line.

The ocean is to the right of the buildings. A building has an ocean 
view if the building can see the ocean without obstructions. Formally, 
a building has an ocean view if all the buildings to its right have a 
smaller height.

Return a list of indices of buildings that have an ocean view, sorted 
in increasing order.
'''

### U - Understand
'''
1. What does it mean for a building to have "no obstructions" to the
   ocean - does it just need to be taller than its immediate neighbor,
   or taller than every single building to its right?
2. Since the ocean is only on the right side, does scanning from left
   to right or from right to left make it easier to know, at each
   building, the tallest building among everything to its right?
'''

### P - Plan
'''
1. Create an empty list to collect the indices of buildings with an
   ocean view.
2. Keep track of the tallest height seen so far while scanning, starting
   at 0 before any buildings have been checked.
3. Scan the heights list from the last index down to the first index,
   since we need to know what's to the right of each building before
   we can judge it.
4. At each index, compare that building's height to the max height
   seen so far (i.e. the tallest building to its right).
5. If the current building is taller than that max, it has an
   unobstructed ocean view: append its index to the results list.
6. Update the max height seen so far to the current building's height,
   since it's now the tallest building to the right of anything further left.
7. If the current building is not taller than the max, it's blocked,
   so skip it and move to the next index without changing the max.
8. Once the scan finishes, the results list was built back-to-front
   (right to left), so reverse it to get indices in increasing order.
9. Return the reversed results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set result = empty list
    set max_height = 0

    FOR i FROM length(heights) - 1 DOWN TO 0:
        IF heights[i] > max_height:
            append i to result
            set max_height = heights[i]

    reverse result
    RETURN result
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_buildings(heights):
	result = []
	max_height = 0
	for i in range(len(heights) - 1, -1, -1):
		if heights[i] > max_height:
			result.append(i)
			max_height = heights[i]
	result.reverse()
	return result
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
xplanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
'''
print(find_buildings([4,2,3,1]))

'''
Example #2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
'''
print(find_buildings([4,3,2,1]))

'''
Example #1:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
'''
print(find_buildings([1,3,2,4]))