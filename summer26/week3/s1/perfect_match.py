##############################
# Problem 1: Perfect Match   #
##############################

# Add code to your IDE so that your program prints 
# out the following to the console:

# Peanut butter and Jelly are a perfect match.
# Spongebob and Patrick are a perfect match.
# Ash and Pikachu are a perfect match.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How do we create a dictionary?
#   The for loop given to us, what is being extracted?

### P - Plan
#   create a dictionary with the missing items
#   pass the dictionary into the function 

# 3. Translate each sub-problem into pseudocode:
#   dict = {"key" : "value", ...}
#   match_made(dict)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def match_made(dictionary):
    for key, value in dictionary.items():
        print( f"{key} and {value} are a perfect match.")

dictionary = {"Peanut butter" : "Jelly", "Spongebob" : "Patrick", "Ash" : "Picachu"}
match_made(dictionary)