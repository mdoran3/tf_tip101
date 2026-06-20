######################################
# Problem 2: Two Pointer Palindrome  #
######################################

'''
Write a function is_palindrome() that takes in a string s 
as a parameter and returns True if the string is a palindrome 
and False otherwise. You may assume the string contains only 
lowercase alphabetic characters.

The function must use the two-pointer approach, which is a 
common technique in which we initialize two variables 
(also called a pointer in this context) to track different 
indices or places in a list or string, then moves the 
pointers to point at new indices based on certain conditions. 
In the most common variation of the two-pointer approach, we 
initialize one variable to point at the beginning of a list 
and a second variable/pointer to point at the end of list. 
We then shift the pointers to move inwards through the list 
towards each other, until our problem is solved or the 
pointers reach the opposite ends of the list.
'''

### U - Understand 
#   What is the advantage of using two pointers?
#   When would we return False?

### P - Plan
#   create start and end pointers at 0 and last index of the string respectively
#   start a while loop that continues while start is less than or equal to the end
#   if the string at the start and end are not equal, return False
#   otherwise, increment the start and decrement the end each by one
#   return True if the while loop completes

# 3. Translate each sub-problem into pseudocode:
'''
    func(str)
        start, end = 0, len(str)-1
        while start is less than or equal to end:
            if str[start] != str[end]:
                return False
            start ++
            end --
        return True
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_palindrome(s):
    start = 0
    end =len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))


'''

Example Output:

True
False

'''