### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What items do we need to keep track of?
    # What build in Python function will be helpful here?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create to variables longest and current and set them to 1 
        # This is because we know the longest we will get is at least 1 (given a nonempty string)
    # Iterate through the sting's range and compare is current index with the previous. 
    # If they are equal the increment current
    # Run a max function comparing current and longest and save the result to longest
    # If they are not equal, reset current to 1
    # Return longest

# 3. Translate each sub-problem into pseudocode:
    # func(str)
        # longest = 1 current = 1
        # for loop in range 1 to length of str
            # if str at current index == str at prev index
                # current += 1
                # max between current and longest = longest
            # else
                # current += 1
        # return longest

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function longest_uniform_substring() that takes in a string s 
# and returns the length of the longest uniform substring. A uniform 
# substring consists of a single repeated character.

def longest_uniform_substring(s):
    longest = 1
    current = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)