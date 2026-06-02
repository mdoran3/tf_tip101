##########################
# PROBLEM 1: LONG PRESSED
##########################

# Write a function is_long_pressed() that takes in a string name 
# and a string typed as parameters. Imagine your friend is typing 
# their name into a keyboard and when typing a character, the key 
# might get long pressed and the character will be typed 1 or more 
# times.

# The function should examine the typed characters and return True 
# if it is possible that it was your friends name with some characters 
# being long pressed and False otherwise.

# Use the two-pointer approach to solve the problem, which is a 
# common technique in which we initialize two variables (also called 
# a pointer in this context) to track different indices or places in 
# a list or string, then moves the pointers to point at new indices 
# based on certain conditions. A common variation of this technique 
# is to point one variable at the beginning of one string and a second 
# pointer at the beginning of a second string, then increment each 
# pointer conditionally to solve a problem.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What condition will make this function return False?
    # Are there any other conditions that will make it False?
    # When should pointers be moved?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Declare to pointers - one for name and one for typed
    # If name equals typed, return True since equal strings are True under the givens
    # Create a while loop and continue until the name pointer is higher than length of name 
        # same logic for type (use AND logic)
    # If name as repeasted chars but typed does not, we automatically return False
    # Else we keep moving forward and update the pointers as follows:
        # if name[i] == name [i-1] then pointer 1 goes up by 2 indices while pointer 2 goes up by 1
        # If typed[i] == typed[i-1] then pointer 2 goes up by 2 indices while pointer1 goes up by one
        # else just increment pointer 1 and pointe 2 each by 1
    # return True outside of the while loop

# 3. Translate each sub-problem into pseudocode:
    # pointer1 = 1
    # pointer2 = 1
    # if name equals type: {return True}
    # while pointer1 <= length of name AND pointer2 <= length of typed
        # if name at pointer1 EQUALS name at pointer1 -1 AND typed at pointer2 NOT EQUAL to typed at pointer2 -1:
            # {return False}
        #elif name at pointer1 EQUALS name at pointer1 -1
            # pointer1 += 2
            # pointer2 += 1
        #elif typed at pointer2 EQUALS typed at pointer2 -1
            # pointer1 += 1
            # pointer2 += 2
        #else
            # pointer1 += 1
            # pointer2 += 1

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_long_pressed(name, typed):
    p1 = 1
    p2 = 1

    if name == typed:
        return True

    while p1 <= len(name)-1 and p2 <= len(typed)-1:
        if name[p1] == name[p1-1] and typed[p2] != typed[p2-1]:
            return False
        elif name[p1] == name[p1-1]:
            p1 += 2
            p2 += 1
        elif typed[p2] == typed[p2-1]:
            p1 += 1
            p2 += 2
        else:
            p1 += 1
            p2 += 1
    return True
    
name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

##############################
# PROBLEM 2: SHARING COOKIES
##############################

# Imagine you're an awesome babysitter and want to give the kids you're 
# looking after some cookies as a snack.
# Each child i has a greed factor g[i], which is the minimum size of a 
# cookie that the child will be content with.
# Each cookie j has a cookie size s[j].
# If s[j] >= g[i], we can assign the cookie j to the child i, and the 
# child will be content.
# If s[j] < g[i], the child will not be content.

# Write a function find_content_children() that takes in the greed list
# g and the cookie size list s as parameters and maximizes the number of 
# content children you are babysitting! The function returns

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Which array gives us the quantity of children?
    # What if the satisfied array is bigger than the greed array?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set 3 variables for children, count of satisfied children, and position
    # Make a while loop for while there are still children left to check if they are satisfied
        # if the 0th position of the s array is greater than or equal to the 0th position of the g array, 
            # then count gets incremented by 1
        # increment position by 1
        # increment children by 1
    # return count

# 3. Translate each sub-problem into pseudocode:
    # children, count, pos = 0
    # while children < length of g
        # if s[pos] >= g[pos]
            # increment count by 1
        # increment pos by 1
        # increment children by 1
    # return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_content_children(s, g):
    children = 0
    count = 0
    pos = 0
    while children < len(g):
        if s[pos] >= g[pos]:
            count += 1
        pos += 1
        children += 1
    return count

g = [1,2,3]
s = [1,1,3]
# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

print(find_content_children(s, g))
# Output: 2 

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

print(find_content_children(s, g))
# Output: 2 

##############################
# PROBLEM 3: VALID PALINDROME
##############################

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

#####################################
# PROBLEM 4: POSITIVE NEGATIVE PAIRS
#####################################

# Write a function find_largest_k() that takes in a list of 
# integers nums that does not contain any zeroes as a parameter. 
# The function finds the largest positive integer k such that -k 
# also exists in the array and returns k. If there is no such 
# integer, return -1.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Should we initially check for both negatives and positives?
    # Do we need a helper function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # for loop for each number in nums
    # if number is less than 0:
    # if the helper function finds the flipped sign of number in the array, return True
    # else if its pair is not found in helper function, return False
    # back in your main function, if the opposite pair is found, return the number times -1
    # if nothing found ever, return -1

# 3. Translate each sub-problem into pseudocode:

    # def helper_function(num)
        # flipped_num = num * -1
        # if flipped_num in nums
            # return TRUE
        # return FALSE

    # for num in nums
        # if num is not negative    
            # if num thrown into help_function(num) returns TRUE
                # return num * -1
    # return -1
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

def find_largest_k(nums):
    def positive_exists(num):
        new_num = num * (-1)
        if new_num in nums:
            return True
        return False

    for num in nums:
        if num < 0:
            if positive_exists(num):
                return num*(-1)
    return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))

############################
# PROBLEM 5: GOOD SUBSTRING
############################

# The sliding window technique is an algorithmic technique often used to find a 
# subarray or substring that meets certain criteria. It works by initializing two 
# pointers to point at the start and end of a ‘window’ or subsection of the 
# string/array at a time. The pointers are then incremented to slide the window 
# and examine a different subarray or substring.

# Use the sliding window technique to solve the following problem:

# Write a function count_good_substrings() that takes in a string s as a parameter 
# and returns the number of good substrings of length three. A string is good if 
# there are no repeated characters. A substring is a continuous sequence of 
# characters in a string.
# If there are multiple occurrences of the same substring, every occurrence 
# should be counted.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # How we construct a "window" in Python
    # How does the window move in order to observe different elements or sets of elements?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a set - sets do not allow repeast items
    # Create to pointers, pointer1 = 0 and pointer2 = 3 (the size of the window)
    # Keep track of good substrings using a variable like good_substrings = 0
    # Start a WHILE LOOP that continues as long as pointer2 is less then length of the string
    # Run a FOR LOOP iterationg through each char from pointer1 to pointer2 in the string
    # Add each char to the set. If there are repeats in the set, they will automatically not be added
    # After adding each element from the window pointer1 to pointer2, check to see if the length of the 
        # set is equal to 3
    # If it is equal to 3, add 1 count to the good_substrings variable
    # increment pointer1
    # increment pointer2
    # return good_substrings count

# 3. Translate each sub-problem into pseudocode:
    # length_set = set()
    # good_subtrings variable = 0
    # pointer1 = 0
    # pointer2 = 3
    # while pointer2 <= len(s)
        # for loop in range pointer1 to pointer 2
            # add string[i'th position] to length_set
        # if length of length_set equals 3
            # good_substrings += 1
        # length_set = set() (clearing the set)
        # pointer1 += 1
        # pointer2 += 1
    # return good_substrings

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_good_substrings(s):
    length_set = set()
    good_substrings = 0
    p1 = 0
    p2 = 3
    while p2 <= len(s):
        for i in range(p1, p2):
            length_set.add(s[i])
        if len(length_set) == 3:
            good_substrings += 1
        length_set = set()
        p1 += 1
        p2 += 1
    return good_substrings

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))