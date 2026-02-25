# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How do we find the length of a list?
    # What type of division is this called when we perform n/2? What does it return?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in a list as a parameter
    # Create a variable to keep track of the majority element and set it to None
    # Create a variable to keep track of the count and set it to 0
    # Iterate through each element in the list
    # If the count is 0, update the majority element to be the current element
    # If the current element is the same as the majority element, add 1 to the count
    # If the current element is different from the majority element, subtract 1 from the count
    # Return the majority element
    
# 3. Translate each sub-problem into pseudocode:
    # func(list):
        # majority_element = None
        # count = 0
        # for element in list:
            # if count == 0:
                # majority_element = element
            # if element == majority_element:
                # count += 1
            # else:
                # count -= 1
        # return majority_element

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_majority_element(elements):
    majority_element = None
    count = 0
    for element in elements:
        if count == 0:
            majority_element = element
        if element == majority_element:
            count += 1
        else:
            count -= 1
    return majority_element


elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))