##########################
# Problem 1: Card Class  #
##########################

'''
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Card 
and store it in a variable named card. The Card 
object should have the suit "Spades" and the rank "8".
'''

### U - Understand 
#   What is an object?
#   How many attributes does an object have in the Card() class?

### P - Plan
#   create a variable named "card"
#   set it equal to Card() with the correct parameters for 'suit' and 'rank'

# 3. Translate each sub-problem into pseudocode:
'''
card = Card(param1, param2)
print(card)
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

card = Card("Spades", "8")
print(f"Suit: {card.suit} \nRank: {card.rank}")