##############################
### Problem 1: Sum of Strings
#############################

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What are data types and why might they be important in this problem?
    # What is the difference of 10 and "10" to a computer?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create a variable called sum and set it equal to 0
    # Iterate through the list of strings
    # Cast each string item to and integer
    # Add that integer to the rolling sum variable

# 3. Translate each sub-problem into pseudocode:
    # func(str):
        # sum = 0
        # for loop : list/str
            # cast str to int
            # add int to sum
        # return sum

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
    
# Write a function sum_of_number_strings() that takes in a list of strings 
# nums. Each string is a representations of integers. The function should 
# return the sum of these strings as an integer.

def sum_of_number_strings(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

################################
## Problem 2: Remove Duplicates
################################

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
    # What data structure can we use to easily remove items?
    # Is there more than one way to solve this problem?

### P - Plan
# 2. Write out in plain English what you want to do: 
    # Create an empty list to store the unique values
    # Create a while loop for while the list is still not empty
    # Pop an item of the list and assign it to a variable inside the while loop
    # If the popped variable is not in the unique values list we created, add it to the list
    # Outside the while loop, return the reversed list

# 3. Translate each sub-problem into pseudocode:
    # func(list)
        # uniques {}
        # while loop for list not empty
            # popped = list.pop()
            # if popped not in uniques
                # uniques.append(popped)
        # return reversed uniques

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:

# Write a function remove_duplicates() that takes in a sorted list of 
# integers nums as a parameter and removes all duplicates in the list. 
# The function returns the modified list.

# WITHOUT WHILE LOOP
# def remove_duplicates(nums):
#     uni_nums = set()
#     for num in nums:
#         if num not in uni_nums:
#             uni_nums.add(num)
#     return uni_nums

# WITH WHILE LOOP
def remove_duplicates(nums):
    uni_nums = []
    while nums:
        popped_item = nums.pop()
        if popped_item not in uni_nums:
            uni_nums.append(popped_item)
    return uni_nums[::-1]    

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

################################
### Problem 3: Reverse Letters
################################

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

#########################################
### Problem 4: Longest Uniform Substring
#########################################

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

##############################
### Problem 5: Teemo's Attack
##############################