#############################
# PROBLEM 2: CREATE SQUIRTLE
#############################

# Step 1: Add the print_pokemon definition below to your code on your IDE.

# Step 2: Instantiate an instance of the class Pokemon and store it in a 
# variable named squirtle. The Pokemon instance created should have name 
# "Squirtle" and its types should be ["Water"].

# Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # In the Pokemon class, what are the two different defs
    # What is self? What does it refer to?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # No implementation is needed. 
    # Run the program and print the object. 

# 3. Translate each sub-problem into pseudocode:
    # No implementation needed

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
squirtle.print_pokemon()