##############################
# Problem 6: Has Duplicates  #
##############################

# Write a function has_duplicates() that takes in a list of 
# integers nums and a positive number k as parameters. The 
# function returns True if the list contains any duplicate 
# elements within k (inclusive) indices of each other. In 
# other words, return True if nums[i] has the same value as 
# any of the k neighboring elements to its left or right. 
# If k is greater than the list's length, the solution 
# should check for duplicates in the complete list. The 
# function should return False otherwise.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#	What does it mean to have duplicates within range of K?
#	What data strcuture might be well suited for this problem?

### P - Plan
#	create a set to store duplicates
#	iterate through the entire nums array
#	check to see if the current num is in the duplicates
#	if it is, return true and if not, add it into the duplicates.

# 3. Translate each sub-problem into pseudocode:
#	func(nums, k):
#	window = set()
#	for loop - i in for range of the length of nums:
#		if nums[i] is in window: 
# 			{return True}
#		window.add(nums[i])
#		if i >=k :
#			window.remove(nums[i-k])
#	{return False}

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def has_duplicates(nums, k):
	duplicates = set()
	count = k
	for i in range(0, len(nums)):
		duplicates.add(nums[i])
		forward = i + 1
		while count > 0:
			if forward >= len(nums):
				break
			if nums[forward] in duplicates:
				return True
			else:
				duplicates.add(nums[forward])
				forward += 1
				count -= 1
		duplicates = set()
		count = k
	return False
		

# Alternative (simpler, more conventional) solution: Co-Authored by Claude AI
# Slide a "window" set containing the previous k elements as we scan
# left to right. If the current element is already in the window, we've
# found a duplicate within k indices. Otherwise add it, and drop the
# element that has fallen out of range (more than k indices behind).
def has_duplicates_v2(nums, k):
	window = set()
	for i in range(len(nums)):
		if nums[i] in window:
			return True
		window.add(nums[i])
		if i >= k:
			window.remove(nums[i - k])
	return False


nums = [5, 6, 8, 2, 6, 4, 9]

print("TF SOLUTIONS:")
check1 = has_duplicates(nums, 2)
print(check1)
check2 = has_duplicates(nums, 5)
print(check2)
check3 = has_duplicates(nums, 3)
print(check3)

print("\nCLAUDE AI SOLUTIONS")
check1 = has_duplicates_v2(nums, 2)
print(check1)
check2 = has_duplicates_v2(nums, 5)
print(check2)
check3 = has_duplicates_v2(nums, 3)
print(check3)

# Example Output:

# False
# True
# True