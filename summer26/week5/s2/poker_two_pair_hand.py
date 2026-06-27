##################################
# Problem 1: Poker Two-Pair Hand #
##################################

'''
In poker, players are given a hand of five cards. A player has a 
"two-pair" hand if they have two cards of the same rank and another 
two cards of another rank. The fifth card isn’t used here.

Given the Card class below, write a function is_two_pair() that takes 
in a list player_hand that contains 5 Card objects.

The function returns True if the player has a two pair hand and False 
otherwise.

Cards in the hand are guaranteed to be unique and are guaranteed to 
have on the following suits and ranks:

The suit is one of the following values: 
"Hearts", "Spades", "Clubs", "Diamonds"

The rank is one of the following values: 
'2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
'''

### U - Understand
# 1. What does a "two-pair" hand look like vs. a hand that is NOT two-pair?
#    Two-pair: exactly 2 cards share one rank AND 2 other cards share another rank (e.g. two Aces + two 4s + any 5th card).
#    NOT two-pair: only one pair (e.g. two 4s + Ace + 6 + 7), three-of-a-kind, four-of-a-kind, or no matching ranks at all.

# 2. What data from each Card object do we actually need to determine two-pair?
#    Only card.rank — the suit is irrelevant. We need to count how many ranks appear exactly twice.

### P - Plan
# 1. Create a dictionary `ranks` to track how many times each rank appears in the hand.
# 2. Initialize a `pairs` counter to 0.
# 3. Loop through each card in player_hand:
#    - If the rank is not in `ranks`, add it with count 1.
#    - If the rank is already in `ranks` with count 1, increment to 2 and increment `pairs`.
#    - If `pairs` reaches 2, we've found two pairs — return True immediately.
# 4. After the loop, return False (fewer than 2 pairs found).

# 3. Translate each sub-problem into pseudocode:
'''
ranks = empty dictionary
pairs = 0

for each card in player_hand:
    if card.rank not in ranks:
        ranks[card.rank] = 1
    else if ranks[card.rank] == 1:
        ranks[card.rank] = 2
        pairs += 1
    if pairs == 2:
        return True

return False
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
	ranks = {}
	pairs = 0
	for card in player_hand:
		if card.rank not in ranks:
			ranks[card.rank] = 1
		elif card.rank in ranks and ranks[card.rank] == 1:
			ranks[card.rank] += 1
			pairs += 1
		if pairs == 2:
			return True
	return False
		

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))

'''
Example Output:

True  # Two Aces + Two 4s (+ Unused 6)
False # Two 4s (+ Ace + 6 + 7)
'''