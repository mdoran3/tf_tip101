# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Will we need to iterate through both lists?
    # What are we returning?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in two lists
    # iterate through list a and check if each element is in list b
    # return False if element doesn't exist in list b, otherwise return True
# 3. Translate each sub-problem into pseudocode:
    # func(list_a, list_b):
        # for element in list_a:
            # if element not in list_b:
                # return False
        # return True

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def all_in(list_a, list_b):
    for element in list_a:
        if element not in list_b:
            return False
    return True
