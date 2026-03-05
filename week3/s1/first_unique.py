### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    #  How can a dictionary help us here?
    #  How can we return an index in python?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create and empty dictionary
    # Iterate through the string and if a char is in the dict, add to its count
    # If the char is not in dict, add it to the dict with a count of 1
    # Then iterate through that dict
    # The first item that has a count of 1, return that char's index from the original string
# 3. Translate each sub-problem into pseudocode:
    # func(str):
        # dict = {}
        # for loop of string
            # if char in dict, char += 1
            # else char = 1
        # for loop dict
            # if char item count == 1
                # return string.index(char)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function first_unique_char() that given a string 
# my_str as a parameter, it finds the first non-repeating 
# character in it and returns its index. If it does not 
# exist, then return -1

def first_unique_char(my_str):
    unis = {}
    for char in my_str:
        if char in unis:
            unis[char] += 1
        else:
            unis[char] = 1
    for i in unis:
        if unis[i] == 1:
            return my_str.index(i)
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))