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
        # pointer2 += 2
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