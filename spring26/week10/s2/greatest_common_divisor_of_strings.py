#################################################
# PROBLEM 3: GREATEST COMMON DIVISOR OF STRINGS #
#################################################

# For two strings s and t, we say "t divides s" if and 
# only if s = t + t + t + ... + t + t (i.e., t is concatenated 
# with itself one or more times).

# Given two strings str1 and str2, return the largest string 
# x such that x divides both str1 and str2.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
    # If no common divisor exists, should we return an empty string or None?
    # Can the two strings be the same, and if so, is the answer just the string itself?

### P - Plan
# 2. Write out in plain English what you want to do:
    # first check if a common divisor can even exist by seeing if str1 + str2 equals str2 + str1
    # if they're not equal, return an empty string
    # otherwise, find the gcd of the two string lengths using the euclidean algorithm
    # return the first gcd-length characters of str1 as the answer

# 3. Translate each sub-problem into pseudocode:
    # if str1 + str2 is not equal to str2 + str1, return ""
    # set a to the length of str1, set b to the length of str2
    # while b is not 0, set a to b and b to a mod b
    # return str1 sliced from 0 to a

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# from math import gcd
# def gcd_of_stings(str1, str2):
# 	if str1 + str2 != str2 + str1:
# 		return ""
# 	return str1[:gcd(len(str1), len(str2))]

def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    a, b = len(str1), len(str2)
    while b:
        a, b = b, a % b
    return str1[:a]

# Example #1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
str1 = "ABCABC"
str2 = "ABC"
print(gcd_of_strings(str1, str2))

# Example #2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
str1 = "ABABAB"
str2 = "ABAB"
print(gcd_of_strings(str1, str2))

# Example #3:
# Input: st1 = "LEET", str2 = "CODE"
# Output: ""
st1 = "LEET"
str2 = "CODE"
print(gcd_of_strings(str1, str2))