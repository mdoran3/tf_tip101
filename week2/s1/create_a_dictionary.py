# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is a dictionary and how is it different from a list?
    # How do we create a dictionary in Python?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in two lists, one with keys and one with values
    # Create an empty dictionary
    # Iterate through the keys list and add that the index of that key 
        # and that index in values and add to dictionary
    # reutn the dictionary
# 3. Translate each sub-problem into pseudocode:
    # func(keys, values):
        # dict = {}
        # for i in range(len(keys)):
            # dict[keys[i]] = values[i]
        # return dict

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def create_a_dictionary(keys, values):
    dict = {}
    for i in range(len(keys)):
        dict[keys[i]] = values[i]
    return dict

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']

print(create_a_dictionary(keys, values))
