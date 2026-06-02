# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Do we iterate through boht dicts? Why or why not?
    # What is the data structure of the output?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in two dicts as parameters
    # Create an empty list to store common keys
    # Iterate through the keys of the first dict
    # If a key is also in the second dict, add it to the list
    # Return the list
# 3. Translate each sub-problem into pseudocode:
    # func(dict1, dict2):
        # common_keys = []
        # for key in dict1:
            # if key in dict2:
                # common_keys.append(key)
        # return common_keys

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def keys_in_common(dict1, dict):
    common_keys = []
    for key in dict1:
        if key in dict2:
            common_keys.append(key)
    return common_keys

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = keys_in_common(dict1, dict2)
print(common_list)