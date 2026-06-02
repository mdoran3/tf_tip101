#############################
# PROBLEM 5: CHOOSE POKEMON
#############################

# Update the Pokemon class with a new method choose() that takes 
# in no parameters except self.

# If the Pokemon is caught, the method should print the string
# "<Pokemon name> I choose you!".

# Otherwise, it should print "<Pokemon name> is wild! Catch them 
# if you can!".

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Where should we add the next function?
    # What does the next fucntion do?
    # Will we use logical conditions in this function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a def called choose() with self as the parameter
    # if self.is_caught is true, then print "<Pokemon name> I choose you!"
    # else print "<Pokemon name> is wild! Catch them if you can!"

# 3. Translate each sub-problem into pseudocode:
    # def choose(self)
        # if attribute == True
            # print first statment (use f formatting, don't hardcode the name)
        # else 
            # print other statment (use f formatting, don't hardcode the name)

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

    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()