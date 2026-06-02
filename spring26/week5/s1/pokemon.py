###########################
# PROBLEM 1: POKEMON CLASS
###########################

# Step 1: Copy the following code into your IDE.

# Step 2: Add a line of code (outside of the class) 
# to instantiate an instance of the class Pokemon 
# and store it in a variable named my_pokemon. The 
# Pokemon instance created should have name "Pikachu"
# and its types should be ["Electric"].

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What are objects in Python or Object Oriented Programming?
    # What is instantiation?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # start a new line outside of the Class
    # name a variable called my_pokemon
    # instantiate a pokemon object by setting my_pokemon equal to Pokemon with attributes "Pikachu" and ["Electric"]

# 3. Translate each sub-problem into pseudocode:
    # my_pokemon = Pokemon(attribute1, attribute2)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

my_pokemon = Pokemon("Pikachu", ["Electric"])
print(my_pokemon.name)
print(my_pokemon.types)