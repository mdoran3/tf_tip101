### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # While a two pointer system would be great, lets not get ahead of our abilities. 
        # Can we use two lists?
    # How do we build a string?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create two lists. One for alpha characters and the other for nonalphas
    # Iterate through the string by char. Test char for isalpha. 
    # If isalpha, add to the alpha list, otherwise add the index of the item to the nonalphas list
    # Create a new empty string
    # Use a for loop through length of original string
    # If the index in the for loop equals an index in nonalphas, concatenate a "-" to the string
    # Otherwise concatenate a char from alphas by using .pop() from alphas
    # Return new_string

# 3. Translate each sub-problem into pseudocode:
    # func(str)
        # alphas = [] and symbols = []
        # i = 0 (track the index)
        # for loop for each char in s
            # if char is an alpha
                # alphas.append(char)
                # increment i 
            # else
                # symbols.append(i)
                # increment i
        # create new string = ""
        # for loop the length of s
            # if current index in for loop is in symbols
                # concatenate new string with a "-"
            # else
                # concatenate new string with alphas.pop()
        # return ne string

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function reverse_only_letters() that takes in a string s as a 
# parameter. The function reverses the order of the letters in the string 
# and returns the new string. Non-letter characters should remain in their 
# original positions.

def reverse_only_letters(s):
    alphas = []
    symbols = []
    i = 0
    for char in s:
        if char.isalpha():
            alphas.append(char)
            i += 1
        else:
            symbols.append(i)
            i +=1
    new_string = ""
    for j in range(0, len(s)):
        if j in symbols:
            new_string = new_string + "-"
        else:
            popped = alphas.pop()
            new_string = new_string + popped
    return new_string

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)