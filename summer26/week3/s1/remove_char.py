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