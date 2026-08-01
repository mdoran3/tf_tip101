######################################
# Problem 3: Valid Word Abbreviation #
######################################

'''
A string can be abbreviated by replacing any number of non-adjacent, 
non-empty substrings with their lengths. The lengths should not have 
leading zeros.

For example, a string such as "substitution" could be abbreviated as 
(but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return True if the string 
matches the given abbreviation. Return False otherwise.

A substring is a contiguous non-empty sequence of characters within a 
string.
'''

### U - Understand
'''
1. How should the digits in abbr be interpreted - as a count of characters
   in word to skip over, and what makes a digit sequence invalid
   (leading zero, or replacing zero characters)?
2. Since word and abbr can be different lengths, how do we know the
   abbreviation is a valid match instead of just running out of one
   string before the other?
'''

### P - Plan
'''
1. Set up two pointers, i for word and j for abbr, both starting at 0.
2. Loop while both i and j are still within bounds of their strings.
3. If abbr[j] is a digit, first reject the whole thing if it's a
   leading zero.
4. Otherwise, consume the full run of consecutive digits starting at j,
   building up the number they represent.
5. Advance i forward by that number, since those are the characters in
   word being skipped over/replaced.
6. If abbr[j] is a letter instead, compare it directly to word[i]; if
   they don't match, the abbreviation is invalid.
7. When it's a letter match, advance both i and j by 1.
8. Repeat steps 2-7 until the loop ends because one pointer ran out.
9. Once the loop ends, check that i and j both landed exactly at the
   end of their strings - if only one did, the abbreviation doesn't
   fully account for the whole word (or vice versa), so it's invalid.
10. Return True only if both pointers reached the end at the same time,
    otherwise return False.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set i = 0
    set j = 0

    WHILE i < length(word) AND j < length(abbr):
        IF abbr[j] is a digit:
            IF abbr[j] == '0':
                RETURN False
            set num = 0
            WHILE j < length(abbr) AND abbr[j] is a digit:
                set num = num * 10 + value_of(abbr[j])
                increment j
            increment i by num
        ELSE:
            IF word[i] != abbr[j]:
                RETURN False
            increment i
            increment j

    RETURN (i == length(word)) AND (j == length(abbr))
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def valid_word_abbreviation(word, abbr):
	i = 0
	j = 0
	while i < len(word) and j < len(abbr):
		if abbr[j].isdigit():
			if abbr[j] == '0':
				return False
			num = 0
			while j < len(abbr) and abbr[j].isdigit():
				num = num * 10 + int(abbr[j])
				j += 1
			i += num
		else:
			if word[i] != abbr[j]:
				return False
			i += 1
			j += 1
	return i == len(word) and j == len(abbr)
				
			

#####################
####### TESTS #######
#####################
'''
Example  #1:
Input: word = "internationalization", abbr = "i12iz4n"
Expected Output: True
Explanation: The word "internationalization" can be abbreviated 
as "i12iz4n" ("i nternational iz atio n").

Example #2:
Input: word = "apple", abbr = "a2e"
Expected Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
'''
print(valid_word_abbreviation("internationalization", "i12iz4n"))
print(valid_word_abbreviation("apple", "a2e"))