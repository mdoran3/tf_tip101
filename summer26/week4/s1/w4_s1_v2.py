##############################
# Problem 1: Perfect Number  #
##############################

'''
Write a function is_perfect_number() that takes in a 
positive integer n and returns True if it is a perfect 
number and False otherwise. A perfect number is a 
positive integer that is equal to the sum of its proper 
divisors, excluding itself.

For example, 6 is a perfect number because its divisors 
or 1, 2, and 3 and 1 + 2 + 3 = 6.
'''

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What mathematical operator would be helpful in this problem?
#   What type of loop could we use and why?

### P - Plan
#   Create an empty list to store the divisors
#   Go through all numbers 1 to n-1 and find ones that are divisors
#   Add the divisors to the empty list
#   Sum the list and check if it equals n

# 3. Translate each sub-problem into pseudocode:
'''
    func(n):
        divisors = empty list
        i = n -1
        while n > 0
            if i mod n == 0, append i to divisors
            decrement i by 1
        summation_of_divisors = sum of nums in divisiors list
        if summarion_of_divisors == n
            return True
        else:
            return False
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def is_perfect_number(n):
    divisors = []
    i = n-1
    while i > 0:
        if n % i == 0:
            divisors.append(i)
        i -= 1
    total = sum(divisors)
    return total == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))


'''

Example Output:

True
True
False

'''


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
    start = 0       # 1st pointer
    end =len(s) - 1 # 2nd pointer
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


###################################
# Problem 3: Evaluate Palindrome  #
####################################

'''
The is_palindrome() problem can also be solved without using 
the two-pointer technique (as you may have seen it in previous 
units)! Evaluate the time and space complexity of your 
two-pointer solution.

Then, evaluate the time and space complexity of the following 
solution:
'''

### U - Understand
# 1. Both solutions check if a string is a palindrome, but they do it differently —
#    does the two-pointer approach ever look at the same character more than once?
#       No. Each pointer moves inward exactly once, so every character is visited at most
#       once. It also short-circuits on the first mismatch, skipping the rest entirely.
# 2. The original solution creates a reversed copy of the string with s[::-1] —
#    does that reversed copy persist in memory throughout the comparison?
#       Yes. s[::-1] allocates a new string of length n that stays in memory until the
#       == comparison finishes, giving the original solution O(n) extra space.

### P - Plan
# 3. Translate each sub-problem into pseudocode:
### Which has better time complexity? ###
# Both solutions are O(n) time. The two-pointer traverses at most n/2 characters,
# while the original builds a reverse in O(n) then compares in O(n) — both linear.
# The two-pointer is faster in practice because it can exit early on a mismatch
# and only scans half the string in the worst case, but Big-O is the same: O(n).

### Which has better space complexity? ###
# The two-pointer solution is O(1) space — it only uses two integer variables
# regardless of input size. The original solution is O(n) space because s[::-1]
# allocates a brand-new string of length n. The two-pointer solution wins on space.

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
### TWO POINTER SOLUTION ###
def is_palindrome(s):
    start = 0       # 1st pointer
    end =len(s) - 1 # 2nd pointer
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

### ORIGINAL SOLUTION ###
def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s