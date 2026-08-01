###########################################
# Problem 3: Buildings with an Ocean View #
###########################################

'''
There are n buildings in a line. You are given an list of integers 
heights of size n that represents the heights of the buildings in 
the line.

The ocean is to the right of the buildings. A building has an ocean 
view if the building can see the ocean without obstructions. Formally, 
a building has an ocean view if all the buildings to its right have a 
smaller height.

Return a list of indices of buildings that have an ocean view, sorted 
in increasing order.
'''

### U - Understand
'''
1. What does it mean for a building to have "no obstructions" to the
   ocean - does it just need to be taller than its immediate neighbor,
   or taller than every single building to its right?
2. Since the ocean is only on the right side, does scanning from left
   to right or from right to left make it easier to know, at each
   building, the tallest building among everything to its right?
'''

### P - Plan
'''
1. Create an empty list to collect the indices of buildings with an
   ocean view.
2. Keep track of the tallest height seen so far while scanning, starting
   at 0 before any buildings have been checked.
3. Scan the heights list from the last index down to the first index,
   since we need to know what's to the right of each building before
   we can judge it.
4. At each index, compare that building's height to the max height
   seen so far (i.e. the tallest building to its right).
5. If the current building is taller than that max, it has an
   unobstructed ocean view: append its index to the results list.
6. Update the max height seen so far to the current building's height,
   since it's now the tallest building to the right of anything further left.
7. If the current building is not taller than the max, it's blocked,
   so skip it and move to the next index without changing the max.
8. Once the scan finishes, the results list was built back-to-front
   (right to left), so reverse it to get indices in increasing order.
9. Return the reversed results list.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set result = empty list
    set max_height = 0

    FOR i FROM length(heights) - 1 DOWN TO 0:
        IF heights[i] > max_height:
            append i to result
            set max_height = heights[i]

    reverse result
    RETURN result
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def find_buildings(heights):
	result = []
	max_height = 0
	for i in range(len(heights) - 1, -1, -1):
		if heights[i] > max_height:
			result.append(i)
			max_height = heights[i]
	result.reverse()
	return result
				
			

#####################
####### TESTS #######
#####################
'''
Example #1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
xplanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
'''
print(find_buildings([4,2,3,1]))

'''
Example #2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
'''
print(find_buildings([4,3,2,1]))

'''
Example #1:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
'''
print(find_buildings([1,3,2,4]))