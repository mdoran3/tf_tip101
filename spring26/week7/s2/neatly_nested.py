############################
# PROBLEM 1: NEATLY NESTED
############################

# Given a string, return True if it is a nesting of zero or 
# more pairs of parentheses. Return False otherwise. A valid 
# pair of parentheses is defined as (). The input string will 
# only contain the characters ( or ). Your solution must be 
# recursive.

# Evaluate the time and space complexity of your solution.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How can we use the replace() method here?
    # Can recrusion help us slowly eliminate our string?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # if the string is equal to the empty string then return True
    # if "()" cannot be found in the string, then we can return False
    # else we return a recursive call by replacing "()" with ""

# 3. Translate each sub-problem into pseudocode:
    # func(string)
        # if string == ""
            # return True
        # if "()" is not in the string:     
            # return False
        # return func(string.replace("()", "", 1))

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_nested(s):
    if s == "":
        return True
    if "()" not in s:
        return False
    return is_nested(s.replace("()", "", 1))

s = "(())"
s1 = "(())("
print(is_nested(s))
print(is_nested(s1))