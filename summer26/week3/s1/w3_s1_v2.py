##############################
# Problem 1: Perfect Match   #
##############################

# Add code to your IDE so that your program prints 
# out the following to the console:

# Peanut butter and Jelly are a perfect match.
# Spongebob and Patrick are a perfect match.
# Ash and Pikachu are a perfect match.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How do we create a dictionary?
#   The for loop given to us, what is being extracted?

### P - Plan
#   create a dictionary with the missing items
#   pass the dictionary into the function 

# 3. Translate each sub-problem into pseudocode:
#   dict = {"key" : "value", ...}
#   match_made(dict)

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def match_made(dictionary):
    for key, value in dictionary.items():
        print( f"{key} and {value} are a perfect match.")

dictionary = {"Peanut butter" : "Jelly", "Spongebob" : "Patrick", "Ash" : "Picachu"}
match_made(dictionary)


##########################
# Problem 2: Remove Char #
##########################

'''
Write a function remove_char() that takes in a 
string s and an integer n as parameters, The 
function returns a new string with the nth 
character removed where 0 < n < len(s).
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   Which way would you select to solve this problem, iterative or slicing?
#   What are we trying to return?

### P - Plan
#   Slice the string from 0 to n
#   concatenate that string with another string from n+1 to the end
#   return this string

# 3. Translate each sub-problem into pseudocode:
#   func(s,n):
#       new_str = s[:n] + s[n+1:]
#       return new_str

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def remove_char(s, n):
    new_str = ""
    count = 0
    for char in s:
        if count != n:
            new_str = new_str + char
        count += 1
    return new_str

# Version 2 - Pythonic
def remove_char_v2(s, n):
    return s[:n] + s[n+1:]
        
s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)

# Example Output: typo


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