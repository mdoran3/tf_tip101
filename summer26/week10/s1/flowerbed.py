########################
# Problem 1: Flowerbed #
########################

'''
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given a list of integers flowerbed containing 0's and 1's, where 0 
means empty and 1 means not empty, and an integer n, return True if 
n new flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule and False otherwise.
'''

### U - Understand
'''
1. What counts as a valid spot to plant a flower, and how do the two ends
   of the flowerbed (index 0 and the last index) affect that check?
2. What should the function return once we know how many flowers can
   actually be planted - a count, or a boolean comparison against n?
'''

### P - Plan
'''
1. Walk through the flowerbed one plot at a time, tracking how many
   flowers have been planted so far.
2. For each empty plot (0), decide whether it's plantable: skip the
   neighbor checks at the two boundary indices, otherwise only plant
   if both the left and right neighbors are empty.
3. After scanning the whole flowerbed, compare the planted count to n
   and return True if they match, False otherwise.
'''

# 3. Translate each sub-problem into pseudocode:
'''
BEGIN
    set i = 0
    set planted = 0

    WHILE i < length(flowerbed):
        IF flowerbed[i] == 0:
            IF i == 0:
                // boundary case, no left neighbor to check
            ELSE IF i == length(flowerbed) - 1:
                // boundary case, no right neighbor to check
            ELSE IF flowerbed[i-1] == 0 AND flowerbed[i+1] == 0:
                mark flowerbed[i] as planted
                increment planted

        increment i

    IF planted == n:
        RETURN True
    RETURN False
END
'''

### I - Implement
# 4. Translate the pseudocode into Python and share your final answer:
def can_place_flowers(flowerbed, n):
	i = 0
	planted = 0
	while i < len(flowerbed):
		if flowerbed[i] == 0:
			if i == 0:
				pass
			elif i == len(flowerbed) - 1:
				pass
			elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
				flowerbed[i] == 1
				planted += 1
		i += 1
	if planted == n:
		return True
	return False
				
			

#####################
####### TESTS #######
#####################
'''
# Example Input: flowerbed = [1,0,0,0,1], n = 1
# Expected Output: True
'''
fb = [1,0,0,0,1]
n = 1
print(can_place_flowers(fb, n))


'''
# Example Input: flowerbed = [1,0,0,0,1], n = 2
# Expected Output: False
'''
fb = [1,0,0,0,1]
n = 2
print(can_place_flowers(fb, n))