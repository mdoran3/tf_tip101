###########################
# PROBLEM 4: CATCH POKEMON
###########################

# Update the Pokemon class with a new method catch() 
# that takes in no parameters except self.

# The method should update the Pokemon's is_caught attribute 
# to True and not return any value.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Based on the print statements and what you may know about scoping,
        # where should you place the new fucntion?
    # What is this function supposed to do?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Under print_pokemon(), write a new def function called catch()
    # Put the parameter self pass in as a parameter
    # Set is_caught equal to True

# 3. Translate each sub-problem into pseudocode:
    # def catch(self):
        # self.attribute = True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })

    def catch(self):
        self.is_caught = True

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()