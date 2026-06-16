####################################
# Problem 3: Longest Common Prefix #
####################################

'''
Write a function longest_common_prefix() that takes in a 
list of strings strings as a parameter. The function returns 
the longest common prefix (not substring) of all strings and 
if there are none, it returns an empty string "".
'''

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
#   What should we return if the input list is empty?
#   Does the prefix have to appear in every string, or just the majority?

### P - Plan
#   If the list is empty, return ""
#   Use the first string as the starting candidate prefix
#   Compare the prefix against each subsequent word
#   Shrink the prefix one character at a time from the right until the word starts with it
#   If the prefix becomes empty, return "" immediately
#   After checking all words, return the remaining prefix

# 3. Translate each sub-problem into pseudocode:
#   if strings is empty: return ""
#   prefix = strings[0]
#   for each word in strings[1:]:
#       while word does not start with prefix:
#           remove last character from prefix
#           if prefix is empty: return ""
#   return prefix

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Version 2: character-by-character comparison using nested loops (no built-ins)
def longest_common_prefix_v2(strings):
    if not strings:
        return ""
    prefix = ""
    for i in range(len(strings[0])):
        char = strings[0][i]
        for word in strings[1:]:
            if i >= len(word) or word[i] != char:
                return prefix
        prefix += char
    return prefix

strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)

'''
Example Output:

fl
'''