# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Why is it best to use a dict for the return value in this case?
    # What is the asymptotic time complexity of our function do you think? Why?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes in a list as a parameter
    # Create an empty dict to store new keys and frequency counts
    # Iterate through the list
    # If an element is already a key in the dict, add 1 to the value
    # If an element is not a key in the dict, add it as a key with a value of 1
    # Return the dict
# 3. Translate each sub-problem into pseudocode:
    # func(list)
        # frequencies = {}
        # for element in list:
            # if element in frequencies:
                # frequencies[element] += 1
            # else:
                # frequencies[element] = 1
        # return frequencies

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_occurrences(nums):
    frequencies = {}
    for num in nums:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    return frequencies

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))