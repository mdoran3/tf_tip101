############################
# Problem 3: Verify Update #
############################

'''
Step 1: Using the same Card class from Problem 2, 
update your code so that the suit of card is 
"Hearts" instead of "Clubs".

Step 2: Use the print_card() method to verify 
that card was updated.

Expected Output: Ace of Hearts
'''

### U - Understand 
#   Are object mutable or immutable?
#   How can you update a certain attribute of an object?

### P - Plan
#   card.suit = "new_suit"

# 3. Translate each sub-problem into pseudocode:
'''
card = Card("Clubs", "Ace")
card.suit = "Hearts"
card.print_card()
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		
	def print_card(self):
	    print(f"{self.rank} of {self.suit}")
		
card = Card("Clubs", "Ace")
card.suit = "Hearts"
card.print_card()
