################################
# Problem 1: String to Integer #
################################

'''
Write a function string_to_integer_mapping() that takes 
in a string of digits s as a parameter and returns a list 
where each element is the integer value of the corresponding 
digit in the string.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What is casting and how is it down in Python?
#   What is the time and the space complexity of this algorithm?

### P - Plan
#   create an empty list
#   iterate through the string 
#   cast each char to an int and append it to the list
#   return the list

# 3. Translate each sub-problem into pseudocode:
#   func(str):
#       nums = []
#       for char in str:
#           new_int = int(char)
#           append new_int to nums
#       return nums

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def string_to_integer_mapping(s):
    nums = []
    for char in s:
        nums.append(int(char))
    return nums

# Example Input: s="12345"
# Example Output: [1, 2, 3, 4, 5]

s="12345"
print(string_to_integer_mapping(s))


#############################
# Problem 2: Delete Minimum #
#############################

'''
Write a function delete_minimum_elements(nums) 
that takes in a list of integers nums as a parameter 
and continuously removes the minimum element until 
the list is empty. The function returns a new list 
of all the elements in nums in the order in which 
they were removed.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   How will a while loop help us in this problem?
#   How do we initialize the minimum value and why?

### P - Plan
#   create an empty list
#   use a while loop to continute while the nums parameter is not empty
#   use a for loop to iterate through each element and find min on each iteration
#   append each min to the empty list created
#   return that list that was created

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       mins = []
#       while nums:
#           for num in nums:
#               if num < min:
#                   min = num
#           i = nums.index(min)
#           popped = nums.pop(i)
#           mins.append(popped)
#       return mins

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def delete_minimum_elements(nums):
    mins = []
    while nums:
        min = float('inf')
        for num in nums:
            if num < min:
                min = num
        i = nums.index(min)
        popped_min = nums.pop(i)
        mins.append(popped_min)
    return mins

# Simple version Co-authored by Claude AI
def delete_minimum_elements_v2(nums):
    mins = []
    while nums:
        minimum = min(nums)
        nums.remove(minimum)
        mins.append(minimum)
    return mins

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)

nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements_v2(nums)
print(removed_lst)

# Example Output: [1,2,3,3,5,8]

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