############################
# Problem 5: Calculate Tip #
############################

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is a variable and how do we create one in Python?
#   Python is an interpreted language. What does that mean?

### P - Plan

# 2. Write out in plain English what you want to do: 
#   make a print statement
#   inside the print statment, concatenate a hardcoded string with the parameter variable passed in function. 

# 3. Translate each sub-problem into pseudocode:
#   func(name):
#       print(f"message, {name}!"")
#
#   then make sure to call the function after naming a variable

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def greet_user(name):
    print(f"Hello, {name}!")

name = "Michael"
greet_user(name)