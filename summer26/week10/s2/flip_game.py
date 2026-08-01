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