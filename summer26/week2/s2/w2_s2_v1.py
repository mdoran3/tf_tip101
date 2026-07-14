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


##########################
# Problem 7: Make Pairs  #
##########################

# Write a function divide_list() that takes in an integer 
# list nums consisting of 2*n integers as parameters. The 
# function divides nums into n pairs such that:

#       Each element belongs to exactly one pair
#       The elements present in a pair are equal

# Return True if nums can be divided into n pairs, 
# otherwise return False.

### U - Understand 
#   What data strcuture would be usful in this scenario?
#   What are we trying to return in this problem?

### P - Plan
#   create an empty set 
#   iterate through nums
#   if num is in the set, delete that num from the set
#   if num is not in set, add it to the set
#   return T/F if the length of the set is 0

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       pairs = set()
#       for num in nums:
#           if num in pairs:
#               delete num from pairs
#           else:
#               add num to pairs
#       return len(pairs) == 0
 
### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def divide_list(nums):
    pair = set()
    for num in nums:
        if num in pair:
            pair.remove(num)
        else:
            pair.add(num)
    return len(pair) == 0


nums = [3,2,3,2,2,2]
print(divide_list(nums))
### Example Output: True ###
# Explanation: There are 6 elements in nums, 
# so they should be divided into 6 / 2 = 3 pairs. 
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), 
# it will satisfy all the conditions.

nums = [1,2,3,4]
print(divide_list(nums))
### Example Output: False ###
# Explanation: There is no way to divide nums into 
# 4 / 2 = 2 pairs such that the pairs satisfy every condition.


###############################
# Problem 6: Has Many Smaller #
###############################

# Write a function smaller_numbers_than_current() 
# that takes in a list of numbers nums as a parameter. 
# For each nums[i], the function should find out how 
# many numbers in the list are smaller than it. 
# (For each nums[i], count the number of valid j's 
#  such that j!=i and nums[j] < nums[i])

# Return the answers in a list.

### U - Understand 
# 1. Share 2 questions you would ask to help understand the question:
#   What does the sum() function do in Python?
#   What are we returning?

### P - Plan
#   create and empty list
#   run the sum() function with ++1 and iterate through nums
#   if num < num it will add one and then append to the empty list
#   return the list

# 3. Translate each sub-problem into pseudocode:
#   func(nums):
#       lst = []
#       for num in nums
#           count = sum(1 for n in nums if n < num)
#           lst.append(count)
#       return count

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def smaller_numbers_than_current(nums):
    length = len(nums)
    i = 0
    ticks = 0
    count = []
    while i < length:
        curr = nums[i]
        for num in nums:
            if num < curr:
                ticks += 1
        count.append(ticks)
        ticks = 0
        i += 1
    return count

# Co-authored by Claude AI
def smaller_numbers_than_current_v2(nums):
    result = []
    for num in nums:
        count = sum(1 for n in nums if n < num)
        result.append(count)
    return result

# Co-authored by Claude AI
def smaller_numbers_than_current_v3(nums):
    return [sum(1 for n in nums if n < num) for num in nums]

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))
# Example Output: [4,0,1,1,3]

print(smaller_numbers_than_current_v2(nums))
# Example Output: [4,0,1,1,3]

print(smaller_numbers_than_current_v3(nums))
# Example Output: [4,0,1,1,3]