########################################
# Problem 2: Intersection of Two Words #
########################################

'''
Given two lists of integers nums1 and nums2, return a list of 
their intersection. Each element in the result list must be 
unique and you may return the result in any order.
'''

### U - Understand
'''
1. What does "intersection" mean here - a value that appears in both
   lists at least once - and how should duplicate values within a
   single list be handled in the output?
2. Does it matter which list we iterate over first, and how many times
   a value appears in each list (versus just whether it appears at all)?
'''

### P - Plan
'''
1. Figure out which of the two input lists is shorter and which is
   longer, since it's cheaper to loop over the shorter one.
2. Create an empty list to collect the intersection results.
3. Loop through each value in the shorter list one at a time.
4. For each value, check whether it also exists somewhere in the
   longer list.
5. If it exists in the longer list AND hasn't already been added to
   the results (to avoid duplicates), append it to the results list.
6. If it doesn't exist in the longer list, or it's already in the
   results, skip it and move to the next value.
7. After scanning the whole shorter list, return the results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set short = the shorter of nums1 and nums2
    set long = the longer of nums1 and nums2
    set intersections = empty list
    set i = 0

    WHILE i < length(short):
        IF short[i] is in long AND short[i] is not in intersections:
            append short[i] to intersections
        increment i

    RETURN intersections
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def intersection(nums1, nums2):
	short = []
	long = []
	intersections = []
	i = 0
	if len(nums1) < len(nums2):
		short = nums1
		long = nums2
	if len(nums2) <= len(nums1):
		short = nums2
		long = nums1
	while i < len(short):
		if short[i] in long and short[i] not in intersections:
			intersections.append(short[i])
		i += 1
	return intersections
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
Output: [2]
'''
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

'''
Example #2:
Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
Expected Output: [9, 4]
[4, 9] is also an acceptable answer.
'''
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))