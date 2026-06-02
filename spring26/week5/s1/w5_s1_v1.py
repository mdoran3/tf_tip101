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