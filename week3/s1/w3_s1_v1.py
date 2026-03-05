####################################
### Problem 1: Calling Mississippi
####################################

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What are we NOT allowed to do in this problem?
    # What are the inputs?
    # What is the output?

### P - Plan
# 2. Write out in plain English what you want to do: 
    #  Our for loop starts at 1 and then only counts to 5 but not inclusive.
    #  We want to be able to inlcude 5 at the end. This is a classic "Off by One" error.
    #  We can fix list by adding one to our terminal condition in the for loop range. 
# 3. Translate each sub-problem into pseudocode:
    #  func(a):
    #      for num in range(1, a + 1):
    #          print( f"{num} blah")

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
    #  def count_mississippi(limit):
    #      for num in range(1, limit + 1):
    #          print( f"{num} mississippi")

# Call the function so that it prints out the following to 
# the console (without calling the function more than once):

def count_mississippi(limit):
    for num in range(1, limit + 1):
        print( f"{num} mississippi")

count_mississippi(5)

##########################
### Problem 2: Swap Ends
##########################

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

##########################
### Problem 3: Is Pangram
##########################

#### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    #  What python data structure would be particularly useful in this situation?
    #  Should we be keeping track of anything in our function?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Set a variable equal to 0 called count
    # creat a set to store the unique letters
    # iterate through the string char by char
    # If char is a space " ", skip it and continue
    # if the char does not exist in set, add it to set and increase count by 1
    # if after iteation, count == 26, then we know it is an anagram

# 3. Translate each sub-problem into pseudocode:
    # func(str)
        # count = 0
        # alpha = set()
        # for loop (str)
            # if item not in alpa:
                # add to alpha
                # increment count
        # return count == 26

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function is_pangram() that takes in a string my_str 
# as a parameter and returns True if the string is a pangram 
# and False if not. A pangram is a sentence containing every 
# letter in the English alphabet.

def is_pangram(my_str):
    count = 0
    alpha = set()
    for char in my_str:
        new_char = char.lower()
        if new_char == " ":
            continue
        if new_char not in alpha:
            alpha.add(new_char)
            count += 1
    return count == 26
        

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

##############################
### Problem 4: Reverse String
##############################

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # Should we iterate through each char?
    # Is there any easy fucntionality that Python offers?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Use python's [start : stop : step] feature
    # Return the string while operating
# 3. Translate each sub-problem into pseudocode:
    # func(str):
        # return str[::-1]

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
# Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    return my_str[::-1]

my_str = "live"
print(reverse_string(my_str))

#############################
### Problem 5: First Unique
#############################

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