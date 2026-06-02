# PROBLEM 3: VALID PALINDROME

# Write a function valid_palindrome() that takes in a 
# string s as a parameter and returns True if s can be 
# a palindrome after deleting at most one character from 
# it and False otherwise.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Should we use a helper function in this implementation?
    # Since this is an interpreted language, do where should a helper function be placed?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Use a for loop and iterate through each char of the string
    # slice out that char from the string using concatenation and slicing and save string into new variable
    # pass that variable into a helper function is_palindrome(string)
    # Implement a two pointer algorithm to check if the string is a palindrome
    # If there is an instance of a palindrome with the sliced string, return TRUE
    # If after iterating through all slices you find that there are no palindromes, return FALSE

# 3. Translate each sub-problem into pseudocode:

    # def is_palindrome(new string):
        # pointer1 = 0
        # pointer2 = length of new string - 1
        # while pointer1 <= pointer2
            # if new_s[pointer1] is not equal to new_s[pointer2]
                # return FALSE
            # pointer1 += 1
            # pointer2 -= 1
        # return TRUE

    # for i in range(length of string)
        # new string = string[:i] + string[i:]
        # if is_palindrome(new string) == True
            # return True
    # return False

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def valid_palindrome(s):

    def is_palindrome(new_s):
        p1 = 0
        p2 = len(new_s)-1
        # print(f"Test if palindrome: {new_s}")
        while p1 <= p2:
            if new_s[p1] != new_s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    for i in range(len(s)):
        new_s = s[:i] + s[i+1:]
        if is_palindrome(new_s):
            return True
    return False
s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))