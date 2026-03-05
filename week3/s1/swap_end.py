### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What is parsing?
    # What data structure might be helpful to create here?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Return a concatented string
    # Indentify the indexes of 3 parts, the first char,
        # the middle chars, and the last char
    # Return them in a single statement

# 3. Translate each sub-problem into pseudocode:
    # func(str):
        # return str[end] + str[0+1:end-1] + str[0]

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function swap_ends() that accepts a string my_str as a parameter and 
# returns a new string where the first and last characters from my_str are swapped.

# def swap_ends(my_str):

#     str_lst = []
#     for char in my_str:
#         str_lst.append(char)

#     str_lst[-1:-1]

#     temp = str_lst[0]
#     str_lst[0] = str_lst[len(str_lst)-1]
#     str_lst[len(str_lst)-1] = temp

#     new_str = "".join(str_lst)
#     return new_str

def swap_ends(my_str):
    return my_str[len(my_str)-1] + my_str[1:-1] + my_str[0]

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)