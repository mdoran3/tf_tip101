#############################
# PROBLEM 1: BATTLE POKEMON
#############################

#Given the Pokemon class below, copy the code and add it to your IDE.

# Then, write a method attack() that takes in a Pokemon object opponent and 
# decreases opponent's hp by their self's damage amount.

# If damaging the opponent leads to the opponent having an hp of 0 or less, 
# the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

# Otherwise, the function should print out 
# "<Pokemon name> dealt <damage> damage to <opponent name>".

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # In this ne function, how many objects are we dealing with?
    # How do we know how much to decrement the opponent's damage by?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a def called attack that takes in a self object and an opponent object
    # subtract self's damage from the opponents hit points (hp)
    # create and if/else statement
    # if the opponents hp is less than zero:
        # print the statement that they fainted
    # else:
        # print the other statement

# 3. Translate each sub-problem into pseudocode:
    # def attack(self, opponent):
        # opponent_hp -= self.damage
        # if opponent_hp < = 0
            # print(<Opponent name> fainted>
        # else:
            # print(<Pokemon name> dealt <damage> damage to <opponent name>)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			print(f"{opponent.name} fainted")
		else:
		    print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
	
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)