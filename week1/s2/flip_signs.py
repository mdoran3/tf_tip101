def flip_sign(lst):
    return [-item for item in lst]

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

# Tech Fellow Task Instructions 

# Template Questions
### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What operation in math changes the sign of a number?
    # What does the function take in as input and what does it output?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Write a func that takes a list as input
    # Create a new list that is empyty
    # Iterate through each item in the list and flip its sign by multiplying it by -1
    # Append the flipped item to the new list
    # Return the new list
# 3. Translate each sub-problem into pseudocode:
    # func(list):
    #     new_list = []
    #     for each item in list:
    #         flipped_item = item * -1
    #         append flipped_item to new_list
    #     return new_list

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def flip_sign(lst):
    new_lst = []
    for item in lst:
        flipped_item = item * -1
        new_lst.append(flipped_item)
    return new_lst