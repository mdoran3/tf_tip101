###########################
# Problem 3: Count Vowels #
###########################

'''
Write a function is_pangram() that takes in a 
string my_str as a parameter and returns True 
if the string is a pangram and False if not. 
A pangram is a sentence containing every letter 
in the English alphabet.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How can we use utilize a dictionary in this problem?
#   Since we are returning a boolean, What is a pythonic way to check True or False?

### P - Plan
#   create and empty dictionary
#   iterate through the string parameter
#   if the lowered char on each iteration is not in the dict, add it
#   check if the length of the dictionary is 26 (the length of the english alphabet)

# 3. Translate each sub-problem into pseudocode:
#   func(str)
#       alphabet = {}
#       for char in str:
#           if char.lower() not in alphabet and char.lower() doesn't equal a space:
#               add char to alphabet dictionary with value 1
#   return boolean of the alphabet dictionary equal to length of 26

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_pangram(my_str):
    alphabet = {}
    for char in my_str:
        char_l = char.lower()
        if char_l not in alphabet and char_l != ' ':
            alphabet[char_l] = 1
    return len(alphabet) == 26


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


# Example Output:

# True
# False