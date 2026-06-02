# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How many iterations will we need to do in the orst case?
    # What do we return if sum of keys and values is equal?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in a dictionary
    # Iterate through the keys and values of the dictionary and add them together, respectively 
    # If the sum of the keys is greater than the sum of the values, return string "keys"
    # If the sum of the keys is less than the sum of the values, return string "values"
    # If the sum of the keys and values are equal, return string "balanced"
# 3. Translate each sub-problem into pseudocode:
    # func(dict):
        # sum_keys = 0
        # sum_values = 0
        # for key in dict:
            # sum_keys += key
        # for value in dict.values():
            # sum_values += value
        # if sum_keys > sum_values:
            # return "keys"
        # elif sum_keys < sum_values:
            # return "values"
        # else:
            # return "balanced"

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def keys_v_values(dict):
    sum_keys = 0
    sum_values = 0
    for key in dict:
        sum_keys += key
        sum_values += dict[key]
    if sum_keys > sum_values:
        return "keys"
    elif sum_keys < sum_values:
        return "values"
    else:
        return "balanced"
    
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)