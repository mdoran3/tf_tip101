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


##########################
# Problem 2: Print Card  #
##########################
'''
Step 1: Update the Card class with the new method 
print_card() provided below:

Step 2: Create an instance of the class and store 
it in a variable named card. The object should have 
suit "Clubs" and rank "Ace".

Step 3: Then, call the method print_card() on your card.
'''

### U - Understand 
#   Where should the new method be scoped?
#   How do we call print_card() to print the new card object that was created?

### P - Plan
#   paste the print_card() function inside the Card() class
#   outside of the class, create a variable called "card"
#   set "card" equal to a Card() object with the parameters "Ace" and "Clubs"
#   call print_card() on the card object

# 3. Translate each sub-problem into pseudocode:
'''
card = Card("param1", "param2)
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
card.print_card()
	
#   Expected Output: Ace of Clubs


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
