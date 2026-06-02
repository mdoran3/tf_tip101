########################
# PROBLEM 3: IS CAUGHT
########################

# Using your code from Problem 2, update your squirtle Pokemon 
# so that is_caught is updated to True. Use the print_pokemon() 
# function to verify that squirtle's is_caught property was 
# updated.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # If an object is already created, do we need to now create another one?
    # Can we add or modify attributes to an object that has already been instantiated. 

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Use the the name of the object "squirtle" to modify one of its attibutes
    # Use the dot (.) operator to call that attribute
    # Set this attribute "is_caught" to True

# 3. Translate each sub-problem into pseudocode:
    # pokemon_object.attribute = True

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

squirtle = Pokemon("Squirtle", ["water"])
squirtle.is_caught = True
squirtle.print_pokemon()
