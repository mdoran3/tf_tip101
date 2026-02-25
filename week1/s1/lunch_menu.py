from ast import For


def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🍕")

# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
    # What params does the function take? How many?
    # How many variables should be declared in the function?

### P - Plan
#2. Write out in plain English what you want to do: 
  # Write a function that takes one param. The param is then passed into the print statement
  # and concatenated with the string "Lunch today is: "
#3. Translate each sub-problem into pseudocode:
    # func(var) - one param
    #   print "Lunch today is: " + var


### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def print_menu(menu):
    print("Lunch today is: " + menu)

print_menu("🍕")