###############################
# Problem 1: Substring Search #
###############################

'''
Given two strings s and sub, write a function count_substring() 
that returns the number of times the substring sub occurs in s. 
Occurrences should not overlap. A substring is a sequence of 
adjacent characters within a larger string.

Your solution must be recursive.

Evaluate the time complexity of your solution.
'''

### U - Understand
#   What should happen once s becomes shorter than sub?
#   Since matches can't overlap, how far should we advance after
#   finding a match versus not finding one?

### P - Plan
'''
1.  Create function definition and pass in s and sub as parameters
2.  if s is shorter than sub, there's no room for a match, so
    return 0
3.  if s starts with sub, count that as one match and recurse on
    the remainder of s after skipping past the whole matched
    substring, adding 1 to the result
4.  otherwise, recurse on s with its first character removed,
    since no match starts here
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN count_substring(s, sub)
    IF length of s is less than length of sub
        RETURN 0
    IF s starts with sub
        RETURN 1 PLUS count_substring(s with the first len(sub)
            characters removed, sub)
    RETURN count_substring(s with its first character removed, sub)
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def count_substring(s, sub):
	if len(s) < len(sub):
		return 0
	if s.startswith(sub):
		return 1 + count_substring(s[len(sub):], sub)
	return count_substring(s[1:], sub)

print(count_substring("abcdeabcde", "abc"))
'''
Example Usage:

# Example Input: s = "abcdeabcde" sub = "abc"
Example Output:

# Expected Output: 2
# Explanation: 'abc' occurs twice in 'abcdeabcde'

# Time complexity: O(n * m), where n = len(s) and m = len(sub).
# We make up to n recursive calls, and each call does an O(m)
# startswith comparison (plus O(m) slicing when a match is found).
'''