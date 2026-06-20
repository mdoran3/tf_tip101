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