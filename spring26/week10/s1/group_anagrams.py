#############################
# PROBLEM 4: GROUP ANAGRAMS #
#############################

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all 
# the original letters exactly once.

### U - Understand
# 1. Share 2 questions you would ask to help understand the question:
	# Can the input contain empty strings, and should they be grouped together?
	# Are the strings case-sensitive, meaning "Eat" and "eat" would NOT be anagrams?

### P - Plan
# 2. Write out in plain English what you want to do:
	# Create a hashmap where the key is a sorted version of each word
	# and the value is a list of all words that sort to that same key
	# Iterate through strs, sort each word to get its key,
	# and append the word to the corresponding list in the hashmap
	# Return all the values in the hashmap as a list of lists

# 3. Translate each sub-problem into pseudocode:
	# anagram_map = {}
	# for word in strs
		# key = "".join(sorted(word))
		# if key not in anagram_map
			# anagram_map[key] = []
		# append word to anagram_map[key]
	# return list of anagram_map.values()

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def group_anagrams(strs):
	anagrams = []
	for word in strs:
		sorted_word = "".join(sorted(word))
		if not anagrams:
			anagrams.append([word])
		else:
			toggle = 0
			for ana_words in anagrams:
				anagram_sorted = "".join(sorted(ana_words[0]))
				if anagram_sorted == sorted_word:
					ana_words.append(word)
					toggle = 1
					break
			# Check toggle if word has been appended
			if toggle == 0:
				anagrams.append([word])
			# Reset toggle
			if toggle == 1:
				toggle = 0
	return anagrams

# Example #1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
s = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(s))

# Example #2:
# Input: strs = [""]
# Expected Output: [[""]]
s1 = [""]
print(group_anagrams(s1))

# Example #3:
# Input: strs = ["a"]
# Expected Output: [["a"]]
s2 = ["a"]
print(group_anagrams(s2))