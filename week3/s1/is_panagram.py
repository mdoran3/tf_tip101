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